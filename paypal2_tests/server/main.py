import os
import random
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from starlette.responses import HTMLResponse, Response, JSONResponse

from paypal2.client import JsonBadRequest
from paypal2.models.order import OrderMinimalResponse
from paypal2.utility import simple_single_order_create
from paypal2_tests.server.deps import GlobalDeps, PayPalDep
from paypal2_tests.server.model import OrderCreateApiRequest

HERE = os.path.dirname(os.path.abspath(__file__))
RESOURCES_PATH = Path(HERE, "resources")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await GlobalDeps.setup()
    try:
        yield
    finally:
        await GlobalDeps.close()


app = FastAPI(title="Testing server for paypal2 lib", lifespan=lifespan)


@app.get("/")
async def root(pp: PayPalDep):
    return HTMLResponse(
        (RESOURCES_PATH / "index.html").read_text() % {"client_id": pp.client_id, "plan_id": GlobalDeps.PLAN_ID}
    )


@app.get("/app.js")
async def app_js():
    return Response((RESOURCES_PATH / "app.js").read_text(), media_type="application/javascript")


@app.post("/api/order-create", response_model=OrderMinimalResponse)
async def api_order_create(pp: PayPalDep, req: OrderCreateApiRequest):
    unit_value = round(0.5 + 20 * random.random(), 2)
    request = simple_single_order_create(req.id, "some service for order testing", unit_value)
    try:
        response = await pp.order_create(request)
    except JsonBadRequest as e:
        return JSONResponse({"error": e.data}, status_code=e.status)
    return response


@app.post("/api/order-capture/{order_id}", response_model=OrderMinimalResponse)
async def api_order_capture(pp: PayPalDep, order_id: str):
    # NOTE: order_id would be validated to be for the current user or at least a known order in production
    return await pp.order_capture(order_id)
