from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp
from pyinstrument import Profiler
from starlette.middleware.base import (
    BaseHTTPMiddleware,
)


# Middleware class for profiling using pyinstrument
class ProfilingMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
    ):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        profiler = Profiler()
        profiler.start()

        try:
            response = await call_next(request)
            return response
        finally:
            profiler.stop()
            print(profiler.output_text(unicode=True, color=True))
