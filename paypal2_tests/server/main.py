import json
import os
import random
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from starlette.responses import HTMLResponse, Response, JSONResponse

from paypal2.client import JsonBadRequest
from paypal2.integration.order import AbstractOrderCreateProcess, AbstractOrderCaptureProcess
from paypal2.models.order import OrderMinimalResponse
from paypal2.models.payment import CapturedPayment
from paypal2.models.subscription import SubscriptionDetails, SubscriptionTransactionList
from paypal2.utility import simple_single_item_order_create
from paypal2_tests.server.deps import GlobalDeps, PayPalDep, WebHookResults
from paypal2_tests.server.hook import DebugPayPalWebHookProcessor, DebugPayPalWebHookProcessorBase
from paypal2_tests.server.model import OrderCreateApiRequest

HERE = os.path.dirname(os.path.abspath(__file__))
RESOURCES_PATH = Path(HERE, "resources")
DB = dict()  # mock db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await GlobalDeps.setup()
    try:
        yield
    finally:
        await GlobalDeps.close()


app = FastAPI(
    title="Testing server for paypal2 lib",
    lifespan=lifespan,
    root_path=os.environ.get("PAYPAL2_TESTING_SERVER_ROOT_PATH", ""),
)


@app.get("/")
async def root(pp: PayPalDep):
    return HTMLResponse(
        (RESOURCES_PATH / "index.html").read_text()
        % {"client_id": pp.client_id, "plan_id": GlobalDeps.PLAN_ID, "root_path": repr(app.root_path)}
    )


@app.get("/app.js")
async def app_js():
    return Response((RESOURCES_PATH / "app.js").read_text(), media_type="application/javascript")


class OrderCreateProcessTester(AbstractOrderCreateProcess):
    async def _handle_pp_exception(self, e: Exception):
        if isinstance(e, JsonBadRequest):
            raise HTTPException(e.status, json.dumps({"error": e.data}), headers={"Content-Type": "application/json"})

    async def _complete_create(self, order_response: OrderMinimalResponse):
        # NOTE: This should be bound to an account/authenticated-identity in production.
        DB.setdefault("orders", []).append(order_response.id)


@app.post("/api/order-create", response_model=OrderMinimalResponse)
async def api_order_create(pp: PayPalDep, req: OrderCreateApiRequest):
    unit_value = round(0.5 + 10000 * random.random(), 2)
    request = simple_single_item_order_create(req.id, "some service for order testing", unit_value)
    return await OrderCreateProcessTester(pp).run(request)


class OrderCaptureProcessTester(AbstractOrderCaptureProcess):
    async def run(self, order_id: str) -> OrderMinimalResponse:
        async with GlobalDeps.ACID_LOCK:  # mock required db tx properties
            return await AbstractOrderCaptureProcess.run(self, order_id)

    async def _validate_order_id(self, order_id: str):
        if order_id not in DB.setdefault("orders", []):
            raise HTTPException(400, detail="order not found")

    async def _handle_pp_exception(self, e: Exception):
        if isinstance(e, JsonBadRequest):
            raise HTTPException(e.status, json.dumps({"error": e.data}), headers={"Content-Type": "application/json"})

    async def _complete_capture(self, order_response: OrderMinimalResponse):
        DB.setdefault("orders", []).remove(order_response.id)


@app.post("/api/order-capture/{order_id}", response_model=OrderMinimalResponse)
async def api_order_capture(pp: PayPalDep, order_id: str):
    return await OrderCaptureProcessTester(pp).run(order_id)


@app.post("/api/hook")
async def api_hook(pp: PayPalDep, whr: WebHookResults, request: Request):
    raw = await request.body()
    # To capture full message as constant reference.
    # print("body=", raw, ",")
    # print("headers=", dict(request.headers), ",")
    data = await pp.verify_webhook_notification(raw, request.headers)
    print("_WEBHOOK_DATA", data)
    if os.environ.get("PAYPAL2_TESTING_WEBHOOK_PROCESSOR") == "ABSTRACT":
        processor = DebugPayPalWebHookProcessor(pp, whr)  # does not work with simulated notifications
    else:
        processor = DebugPayPalWebHookProcessorBase(whr)
    result = await processor.call(data)
    print("_WEBHOOK_RESULT", result)
    return Response()


@app.post("/api/webhook-results")
async def api_webhook_results(whr: WebHookResults):
    buf = []
    while True:
        try:
            item = whr.popleft()
        except IndexError:
            break
        else:
            buf.append(item)
    return JSONResponse({"results": buf})


@app.post("/api/payment/{payment_id}", response_model=Optional[CapturedPayment])
async def api_payment_details(pp: PayPalDep, payment_id: str):
    return await pp.captured_payment_details(payment_id)


@app.post("/api/subscription/{subscription_id}", response_model=Optional[SubscriptionDetails])
async def api_subscription_details(pp: PayPalDep, subscription_id: str):
    return await pp.subscription_details(subscription_id)


@app.post("/api/subscription-tx/{subscription_id}", response_model=Optional[SubscriptionTransactionList])
async def api_subscription_details(pp: PayPalDep, subscription_id: str):
    return await pp.subscription_transaction_list(subscription_id)
