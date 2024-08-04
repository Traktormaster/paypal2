import asyncio
import json
import re

import aiohttp
import pytest
from pydantic import BaseModel
from pytest_httpserver import HTTPServer
from selenium.webdriver.remote.webdriver import WebDriver
from werkzeug import Request, Response

from paypal2.hook import PayPalWebHookProcessorBase
from paypal2_tests.const import (
    HOOK_CERTS,
    HOOK_PAYMENT_CAPTURE_PENDING_V2,
    HOOK_PAYMENT_CAPTURE_COMPLETED_V2,
    HOOK_PAYMENT_CAPTURE_REFUNDED_V2,
    HOOK_PAYMENT_CAPTURE_REVERSED_V2,
    HOOK_PAYMENT_CAPTURE_DECLINED_V2,
    HOOK_SUBSCRIPTION_CREATED_v1,
    HOOK_SUBSCRIPTION_CREATED_v2,
    HOOK_PAYMENT_SALE_COMPLETED,
    HOOK_SUBSCRIPTION_EXPIRED_V2,
    HOOK_SUBSCRIPTION_CANCELLED_V2,
    HOOK_SUBSCRIPTION_PAYMENT_FAILED_V2,
    HOOK_PAYMENT_SALE_REVERSED,
    HOOK_PAYMENT_SALE_REFUNDED,
    HOOK_PLAN_CREATED_V2,
    HOOK_PLAN_UPDATED_V2,
    HOOK_SUBSCRIPTION_CANCELLED_V1,
    HOOK_PLAN_CREATED_V1,
    HOOK_PLAN_UPDATED_V1,
    HOOK_SUBSCRIPTION_ACTIVATED_v2,
    HOOK_SUBSCRIPTION_SUSPENDED_V2,
)
from paypal2_tests.utility import ServerProc


@pytest.mark.order(10)
@pytest.mark.asyncio
async def test_paypal2_client(server_proc: ServerProc, selenium: WebDriver, httpserver: HTTPServer):
    async with aiohttp.ClientSession() as s:  # Wait for server startup.
        for _ in range(50):
            try:
                async with s.get(server_proc.url) as r:
                    if r.status == 200:
                        break
            except Exception:
                pass
            await asyncio.sleep(0.15)
        else:
            assert False, "Server setup timeout"

    await _webhook_check(server_proc, httpserver)

    selenium.implicitly_wait(5)
    selenium.get(server_proc.url)

    while True:
        await asyncio.sleep(1)


async def _webhook_check(server_proc: ServerProc, httpserver: HTTPServer):
    base_url = httpserver.url_for("")
    translated_cert_map = {k.replace("https://api.paypal.com/", base_url): v for k, v in HOOK_CERTS.items()}

    def handler(req: Request):
        data = translated_cert_map.get(req.url)
        if not data:
            return Response(status=404)
        return Response(data, 200, {"Content-Type": "application/x-pem-file"})

    httpserver.expect_request(re.compile("^/")).respond_with_handler(handler)

    async with aiohttp.ClientSession() as s:

        async def _get_webhook_result(ignore=False):
            async with s.post(server_proc.url + "/api/webhook-results") as r_:
                r_.raise_for_status()
                d_ = await r_.json()
                if not ignore:
                    assert isinstance(d_, dict)
                    assert isinstance(d_.get("results"), list)
                    assert len(d_["results"]) == 1
                    assert isinstance(d_["results"][0], dict)
                    assert set(d_["results"][0].keys()) == {"key", "event"}
                    return d_["results"][0]

        await _get_webhook_result(ignore=True)  # clear remaining if any
        for const_req in [
            HOOK_PAYMENT_CAPTURE_PENDING_V2,
            HOOK_PAYMENT_CAPTURE_COMPLETED_V2,
            HOOK_PAYMENT_CAPTURE_REFUNDED_V2,
            HOOK_PAYMENT_CAPTURE_REVERSED_V2,
            HOOK_PAYMENT_CAPTURE_DECLINED_V2,
            HOOK_SUBSCRIPTION_CREATED_v2,
            HOOK_SUBSCRIPTION_ACTIVATED_v2,
            HOOK_SUBSCRIPTION_SUSPENDED_V2,
            HOOK_SUBSCRIPTION_EXPIRED_V2,
            HOOK_SUBSCRIPTION_CANCELLED_V2,
            HOOK_SUBSCRIPTION_PAYMENT_FAILED_V2,
            HOOK_PAYMENT_SALE_COMPLETED,
            HOOK_PAYMENT_SALE_REVERSED,
            HOOK_PAYMENT_SALE_REFUNDED,
            HOOK_PLAN_CREATED_V2,
            HOOK_PLAN_UPDATED_V2,
            # rest is deprecated, the fallback handler can catch them
            HOOK_SUBSCRIPTION_CREATED_v1,
            HOOK_SUBSCRIPTION_CANCELLED_V1,
            HOOK_PLAN_CREATED_V1,
            HOOK_PLAN_UPDATED_V1,
        ]:
            headers = dict(const_req.headers)
            headers["paypal-cert-url"] = headers["paypal-cert-url"].replace("https://api.paypal.com/", base_url)
            async with s.post(server_proc.url + "/api/hook", data=const_req.body, headers=headers) as r:
                assert r.status == 200
            result = await _get_webhook_result()
            result_key = tuple(result["key"]) if result["key"] is not None else None
            for event_cls, _ in PayPalWebHookProcessorBase().webhook_handlers.values():
                if event_cls.HANDLER_KEY == result_key:
                    event: BaseModel = event_cls.model_validate(json.loads(const_req.body))
                    assert result["event"] == event.model_dump(mode="json")
                    break
            else:
                assert False, f"webhook handler not for {result_key}"
