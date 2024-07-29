import uvicorn


if __name__ == "__main__":
    uvicorn.run("paypal2_tests.server.main:app", host="127.0.0.1", port=8001)
