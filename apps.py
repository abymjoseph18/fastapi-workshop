from fastapi import FastAPI

from routes.ping import health_check_router
from routes.task import task_router
from routes.time import time_router
from routes.hello_world import hello_world_router
from middlewares.profiler import ProfilingMiddleware

app = FastAPI(title="FastAPI workshop", description="Prepared for Fastapi Introduction")

# Add the ProfilingMiddleware to the app
app.add_middleware(ProfilingMiddleware)

app.include_router(time_router)
app.include_router(health_check_router)
app.include_router(hello_world_router)
app.include_router(task_router)

# app.add_route("/graphql", GraphQLApp(schema))
