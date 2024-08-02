# paypal2

Opinionated asyncio Python server-side integration SDK for PayPal. 

# Status

WIP

# Testing

Complete testing requires deploying the repository on a server behind an SSL reverse-proxy, so the web-hook
notifications can be used in sandbox.

1. Installing repo revision in a virtualenv example ("d$" denotes shell on the dev host "r$" is the remote-server host)

        d$ git archive -o paypal2.tgz HEAD
        d$ scp paypal2.tgz remote:
        r$ python3.10 -m venv .paypal2-venv
        r$ source .paypal2-venv/bin/activate
        r$ mkdir paypal2 && cd paypal2 && tar -xf ../paypal2.tgz
        r$ pip install wheel
        r$ pip install -r requirements/test.txt
        r$ pip install --no-deps -e .
2. Setting up a temporary endpoint on an existing domain for testing using nginx. Add the following location snippet to a suitable server. The path prefix may need adjustment, and basic HTTP authentication can be added for safety, although no secret shall be revealed by the dev-api and it may only interface with the sandbox environment. Check the config and reload your nginx as you like.

        location ~ ^/paypal2-dbg/(.*) {
            proxy_set_header X-Real-IP $remote_addr;
            proxy_pass      http://127.0.0.1:8001/$1;
            proxy_read_timeout 120s;
            # ensure no caching for dev
            expires           -1;
            add_header        Cache-Control no-store;
        }
3. Run the dev server with the following script. Some values need adjustment, and you may want to do this in a screen session for convenience.

        source .paypal2-venv/bin/activate
        cd paypal2
        export ALLOW_TESTS_IMPORT=1
        export PAYPAL2_TESTING_SERVER_RUN=1
        export PAYPAL2_TESTING_SERVER_ROOT_PATH=/paypal2-dbg
        export PAYPAL2_TESTING_WEBHOOK_PROCESSOR=ABSTRACT
        export PAYPAL2_TESTING_CLIENT_ID=<YOUR-SANDBOX-APP-ID>
        export PAYPAL2_TESTING_CLIENT_SECRET=<YOUR-SANDBOX-APP-SECRET>
        export PAYPAL2_TESTING_WEBHOOK_ID=<YOUR-SANDBOX-WEBHOOK-ID>
        python -m pytest -vv -s -x -k test_run > ./run.log 2>&1

4. If everything is set up correctly, visiting https://<your-domain>/paypal2-dbg/ will display the dev index where basic order and subscription functionality can be tested along with the relevant webhook notifications if that is configured as well.
