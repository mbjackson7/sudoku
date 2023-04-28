from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
def read_root():
    return {"404": "Not Found"}


@app.get("/start/{difficulty}")
def read_item(difficulty: int, q: Union[str, None] = None):
    return {"difficulty": difficulty, "q": q}