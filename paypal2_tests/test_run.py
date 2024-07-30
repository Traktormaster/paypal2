import os
import time

import pytest

from paypal2_tests.utility import ServerProc


@pytest.mark.skipif(
    os.environ.get("PAYPAL2_TESTING_SERVER_RUN", "").lower() not in ("1", "true", "yes", "on"),
    reason="not running for debug",
)
def test_run_debug(server_proc: ServerProc):
    while True:
        time.sleep(1)
