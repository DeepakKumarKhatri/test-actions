from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# @app.get("/hello/{name}")
# def greet_name(name: str):
#     return {"message": f"Hello, {name}!"}
