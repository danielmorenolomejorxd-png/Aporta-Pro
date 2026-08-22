from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head><title>SPORTIA V8 REAL</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body style="background:#0a0a0a;color:#00ff88;font-family:Arial;padding:20px;text-align:center">
    <h1>🚀 SPORTIA V8 REAL</h1>
    <h2 style="color:white">✅ ¡FUNCIONA FERNANDO!</h2>
    <div style="background:#1a1a1a;padding:15px;border-radius:10px;margin:20px 0;text-align:left">
    <p>⚽ Barcelona vs Real Madrid - Cuota 1.85</p>
    <p>⚽ Man City vs Arsenal - Cuota 2.10</p>
    <p>⚽ Bayern vs Dortmund - Cuota 1.95</p>
    </div>
    <button onclick="alert('¡TELEGRAM CONECTADO!')" style="background:yellow;color:black;padding:20px;font-size:20px;border:none;border-radius:10px;width:100%">🚨 PROBAR TELEGRAM</button>
    <p style="color:gray;margin-top:20px">Railway: ONLINE</p>
    </body>
    </html>
    """

@app.get("/test")
def test():
    return {"status": "OK", "message": "SPORTIA funciona"}
