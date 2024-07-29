import os
import subprocess
import sys

import pytest_asyncio

from paypal2_tests.utility import ServerProc


@pytest_asyncio.fixture
async def server_proc():
    assert os.environ.get("PAYPAL2_TESTING_CLIENT_ID")
    assert os.environ.get("PAYPAL2_TESTING_CLIENT_SECRET")
    server_p = subprocess.Popen([sys.executable, "-m", "paypal2_tests.server"])
    try:
        yield ServerProc(proc=server_p, url="http://127.0.0.1:8001")
    finally:
        if server_p.poll() is None:
            server_p.terminate()
            server_p.wait()
