from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
from sudokuGame import SudokuGame 
import os
import uvicorn
import time

app = FastAPI()

games = {}

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/start/{id}/{difficulty}")
def start(id: str, difficulty: int):
    for key in games:
        if games[key].gameOver or games[key].lastUpdated < time.time() - 86400:
            games.pop(key)
    if id in games.keys():
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
    
@app.get("/solve/{id}")
def solve(id: str):
    if id in games:
        games[id].solve()
        data = {"board": games[id].get_2d_board()}
        if games[id].gameOver:
            games.pop(id)
        return data
    else:
        return {"error": "Game ID does not exist"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", default=5000)), log_level="info")