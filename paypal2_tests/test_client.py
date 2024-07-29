import asyncio

import aiohttp
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from paypal2_tests.utility import ServerProc


@pytest.mark.asyncio
async def test_paypal2_client(server_proc: ServerProc, selenium: WebDriver):
    async with aiohttp.ClientSession() as s:  # Wait for server startup before selenium access.
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

    selenium.implicitly_wait(5)
    selenium.get(server_proc.url)

    while True:
        await asyncio.sleep(1)
