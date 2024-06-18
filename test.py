import fastapi


app = fastapi.FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/name/")
def create_user(name: str):
    return {"name": name}
