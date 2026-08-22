from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api/predict/{player1}/{player2}")
async def predict(player1: str, player2: str):
    return {"player1": player1, "player2": player2, "prediction": f"{player1} 68% gana vs {player2}", "confidence": "68%"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
