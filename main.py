from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def home():
    return HTMLResponse("""
    <html><body style="background:#0a0a0a;color:white;font-family:sans-serif;text-align:center;padding:50px">
    <h1>🏓 SportIA Pro - LIVE WTT</h1>
    <h2 style="color:#00ff88">¡App Funcionando!</h2>
    <p>AI Predicción Tenis de Mesa WTT</p>
    <a href="/docs" style="color:#00ff88">Ver API /docs</a>
    </body></html>
    """)

@app.get("/api/status")
def status():
    return {"status":"online","sport":"WTT Table Tennis","version":"1.0"}
