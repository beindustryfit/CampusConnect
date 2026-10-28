"""Campus Connect API.

Week 1: add GET /health that returns {"status": "ok"}.
Do not delete the GET / route. The starter test needs it.
"""
from fastapi import FastAPI

app = FastAPI(title="Campus Connect")


@app.get("/")
def root():
    return {
        "app": "campus-connect",
        "hint": "Week 1: add GET /health that returns status ok",
    }
