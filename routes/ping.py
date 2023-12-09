from fastapi import APIRouter

health_check_router = APIRouter()

@health_check_router.get(
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
