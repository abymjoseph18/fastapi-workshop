from fastapi import FastAPI, Depends
from datetime import datetime

app = FastAPI(title="FastAPI workshop", description="Prepared for Fastapi Introduction")


# Define a route using a decorator
@app.get("/", summary="Hello, World!", description="A simple 'Hello, World!' example.")
def root():
    return {"message": "Hello, FastAPI Workshop!"}


def get_current_time():
    return datetime.now()


@app.get(
    "/ping",
    summary="Ping the server",
    description="Returns a simple 'pong' message to check if the server is running.",
    response_description="Text response with 'pong'.",
    tags=["Health checks"]
)
async def ping():
    """
    Ping the server to check if it's running.
    """
    return "pong"


@app.get(
    "/get-current-time",
    summary="Get the current time",
    description="Returns the current date and time as a JSON response.",
    response_description="JSON response containing the current time.",
    tags=["Time"])
async def read_current_time(current_time: datetime = Depends(get_current_time)):
    return {"current_time": current_time}
