from fastapi import FastAPI
from typing import Union
from sudokuGame import SudokuGame 
import time

app = FastAPI()

games = {}

@app.get("/")
def read_root():
    return {"404": "Not Found"}

@app.get("/start/{id}/{difficulty}")
def read_item(id: str, difficulty: int, q: Union[str, None] = None):
    for id in games:
        if games[id].gameOver or games[id].lastUpdated < time.time() - 86400:
            games.pop(id)
    if id in games:
        return {"error": "Game ID already exists"}
    else:
        games[id] = SudokuGame(difficulty)
        return {"board": games[id].get_2d_board(), "remaining": games[id].remaining, "max_strikes": games[id].maxStrikes}

@app.get("/check/{id}/{row}/{col}/{value}")
def check(id: str, row: int, col: int, value: int):
    if id in games:
        games[id].check(row, col, value)
        data = {"board": games[id].get_2d_board(), "remaining": games[id].remaining, "strikes": games[id].strikes, "game_over": games[id].gameOver}
        if games[id].gameOver:
            games.pop(id)
        return data
        
    else:
        return {"error": "Game ID does not exist"}

@app.get("/hint/{id}")
def hint(id: str):
    if id in games:
        games[id].hint()
        data = {"board": games[id].get_2d_board(), "remaining": games[id].remaining, "game_over": games[id].gameOver}
        if games[id].gameOver:
            games.pop(id)
        return data
    else:
        return {"error": "Game ID does not exist"}

@app.get("/resume/{id}")
def resume(id: str):
    if id in games:
        return {"board": games[id].get_2d_board(), "remaining": games[id].remaining, "max_strikes": games[id].maxStrikes, "strikes": games[id].strikes, "time": games[id].startTime}
    else:
        return {"error": "Game ID does not exist"}