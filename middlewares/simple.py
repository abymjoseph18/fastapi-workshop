from starlette.middleware.base import (
    BaseHTTPMiddleware,
)
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp


class SimpleMiddleware(BaseHTTPMiddleware):
    def __init__(
            self,
            app: ASGIApp,
    ):
        super().__init__(app)

    async def dispatch(
            self, request: Request, call_next
    ) -> Response:
        # Code to be executed before the request is processed
        print("Before processing the request")

        response = await call_next(request)

        # Code to be executed after the request is processed
        print("After processing the request")
        return response
