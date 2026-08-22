import os, requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from datetime import datetime
import pytz

BOT_TOKEN = os.getenv("BOT_TOKEN", "8972036325:AAHsRubJ1s2wq_LhIe7mmyMBanpeRQuu-tQ")
CHAT_ID = os.getenv("CHAT_ID", "8760042926")
app = FastAPI()

def send_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}, timeout=10)
        return True
    except: return False

PREDICCIONES = [
    {"live": "LIVE WTT CHAMPIONS", "set": "BO5 - Set 3", "match": "Harimoto [3] vs Fan Zhendong [1]", "ia": "45% Fan Zhendong gana", "cuota_ia": "2.04", "bookie": "1.47", "value": "+12%"},
    {"live": "LIVE WOMEN FINAL", "set": "BO7 - Set 5", "match": "Sun Yingsha [1] vs Wang Manyu [2]", "ia": "64% Sun Yingsha gana", "cuota_ia": "1.44", "bookie": "1.35", "value": "+18%"},
    {"live": "PROXIMO - 14:30", "set": "WTT Star Contender", "match": "Calderano [4] vs Moregard [12]", "ia": "75% Calderano", "cuota_ia": "1.23", "bookie": "1.85", "value": "+8%"}
]

@app.get("/", response_class=HTMLResponse)
def home():
    tz = pytz.timezone('America/Bogota')
    now = datetime.now(tz).strftime("%d/%m %H:%M:%S")
    html = f"<html><head><meta name='viewport' content='width=device-width, initial-scale=1'><style>body{{background:#0f0f0f;color:white;font-family:Arial;padding:10px}}.header{{background:linear-gradient(90deg,#00ff88,#00ccff);color:black;padding:20px;border-radius:20px;text-align:center}}.card{{background:#1e1e1e;border-radius:15px;padding:15px;margin:15px 0}}.value{{background:#00ff8840;color:#00ff88;padding:5px 10px;border-radius:10px;float:right}}.btn{{background:#ffcc00;color:black;padding:15px;text-align:center;border-radius:10px;font-weight:bold;display:block;text-decoration:none;margin:10px 0}}</style></head><body><div class='header'><h1>🏓 SportIA Pro V4</h1><div>IA + BOT ACTIVO</div><small>Online: {now}</small></div>"
    for p in PREDICCIONES:
        html += f"<div class='card'><small style='color:#ff4444'>● {p['live']}</small><small style='float:right'>{p['set']}</small><h2>{p['match']}</h2><div style='color:#00ff88;font-size:20px;font-weight:bold'>🤖 IA: {p['ia']}</div><div>Cuota IA: {p['cuota_ia']} Bookie: {p['bookie']} <span class='value'>VALUE {p['value']}</span></div></div>"
    html += "<a class='btn' href='/test-bot'>🚨 PROBAR BOT TELEGRAM AHORA</a><a class='btn' style='background:#00ff88' href='/api/predictions'>📊 VER PREDICCIONES API</a></body></html>"
    return html

@app.get("/test-bot")
def test_bot():
    msg = "🚨 <b>SPORTIA PRO V4 - ALERTA VALUE</b> 🚨\n\n🏓 <b>Sun Yingsha vs Wang Manyu</b>\n🤖 IA: 64% Sun Yingsha\n💰 VALUE +18%\n\n¡Bot funcionando Fernando! 🔥"
    ok = send_telegram(msg)
    return HTMLResponse(f"<h1>{'✅ ENVIADO' if ok else '❌ ERROR'}</h1><p>Revisa Telegram @sportia_pro_v3_bot</p><a href='/'>Volver</a>")

@app.get("/api/predictions")
def api(): return {"status": "V4 BOT ACTIVO", "predictions": PREDICCIONES}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
