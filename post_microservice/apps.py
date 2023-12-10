from starlette_graphene3 import GraphQLApp
from fastapi import FastAPI

from post_microservice.graphql_schema import schema
from graphql_explorer.fastapi import router


app = FastAPI()
app.add_route("/graphql", GraphQLApp(schema))

app.include_router(router)
