from datetime import datetime

from fastapi import Depends, APIRouter

time_router = APIRouter()


def get_current_time():
    return datetime.now()


@time_router.get(
    "/get-current-time",
    summary="Get the current time",
    description="Returns the current date and time as a JSON response.",
    response_description="JSON response containing the current time.",
    tags=["Time"],
)
async def read_current_time(current_time: datetime = Depends(get_current_time)):
    return {"current_time": current_time}
