from fastapi import FastAPI

app = FastAPI()


# Define a route using a decorator
@app.get("/")
def root():
    return {"message": "Hello, FastAPI Workshop!"}
