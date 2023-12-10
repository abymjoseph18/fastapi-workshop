from fastapi import APIRouter

hello_world_router = APIRouter()


# Define a route using a decorator
@hello_world_router.get(
    "/", summary="Hello, World!", description="A simple 'Hello, World!' example."
)
def root():
    return {"message": "Hello, FastAPI Workshop!"}
