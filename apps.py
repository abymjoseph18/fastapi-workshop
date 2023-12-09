from fastapi import FastAPI

app = FastAPI(title="FastAPI workshop", description="Prepared for Fastapi Introduction")


# Define a route using a decorator
@app.get("/")
def root():
    return {"message": "Hello, FastAPI Workshop!"}
