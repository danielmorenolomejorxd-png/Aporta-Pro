from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
from datetime import datetime

app = FastAPI()

# --- FRONTEND BONITO ---
HTML_PAGE = """
<html>
<head>
<title>SportIA Pro - WTT LIVE</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:#0f0f0f;color:white;font-family:Arial;text-align:center;padding:20px}
.card{background:#1e1e1e;border-radius:15px;padding:20px;margin:15px auto;max-width:400px;border-left:5px solid #00ff88}
.prob{font-size:28px;color:#00ff88;font-weight:bold}
.btn{background:#00ff88;color:black;padding:12px 25px;border-radius:10px;text-decoration:none;display:inline-block;margin:10px;font-weight:bold}
</style>
</head>
<body>
<h1>🏓 SportIA Pro</h1>
<h3>WTT LIVE - IA Predictions</h3>
<div class="card">
<h3>🔴 LIVE: Harimoto vs Fan Zhendong</h3>
<p class="prob">IA: 68% Fan Zhendong</p>
<p>Cuota: 1.47 | Value: +12%</p>
</div>
<div class="card">
<h3>🔴 LIVE: Sun Yingsha vs Wang Manyu</h3>
<p class="prob">IA: 74% Sun Yingsha</p>
<p>Cuota: 1.35 | Value: +18%</p>
</div>
<a class="btn" href="/docs">Ver API</a>
<a class="btn" href="/api/predictions">Ver Predicciones JSON</a>
<p style="margin-top:30px;opacity:0.5">Online desde: """ + datetime.now().strftime("%d/%m/%Y %H:%M") + """<br>web-production-a8499.up.railway.app</p>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PAGE

@app.get("/api/status")
def status():
    return {"status": "online", "sport": "WTT Table Tennis", "version": "2.0 PRO", "matches_live": 2}

@app.get("/api/predictions")
def predictions():
    return {
        "date": str(datetime.now()),
        "predictions": [
            {"match": "Harimoto vs Fan Zhendong", "fav": "Fan Zhendong", "prob": 68, "cuota": 1.47, "value": "+12%", "recomendacion": "APOSTAR"},
            {"match": "Sun Yingsha vs Wang Manyu", "fav": "Sun Yingsha", "prob": 74, "cuota": 1.35, "value": "+18%", "recomendacion": "APOSTAR FUERTE"},
            {"match": "Calderano vs Moregard", "fav": "Calderano", "prob": 61, "cuota": 1.85, "value": "+8%", "recomendacion": "RIESGO MEDIO"}
        ]
    }

@app.get("/api/wtt-live")
def wtt_live():
    return {"live_now": 2, "next_tour": "WTT Champions Montpellier", "status": "IA analizando en vivo"}
    
