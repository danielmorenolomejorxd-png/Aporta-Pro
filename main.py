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

@app.get("/", response_class=HTMLResponse)
def home():
    tz = pytz.timezone('America/Bogota')
    now = datetime.now(tz).strftime("%d/%m %H:%M:%S")
    return f"""
    <html><head><meta name='viewport' content='width=device-width'><style>
    body{{background:#0f0f0f;color:white;font-family:Arial;padding:15px}}
    .header{{background:linear-gradient(90deg,#00ff88,#00ccff);color:black;padding:20px;border-radius:20px;text-align:center}}
    .card{{background:#1e1e1e;border-radius:15px;padding:15px;margin:15px 0}}
    .btn{{background:#ffcc00;color:black;padding:18px;text-align:center;border-radius:12px;font-weight:bold;display:block;text-decoration:none;margin:15px 0;font-size:18px}}
    </style></head><body>
    <div class='header'><h1>🏓 SportIA Pro V4</h1><p>BOT ACTIVO ✅ {now}</p></div>
    <div class='card'><h2>Harimoto vs Fan Zhendong</h2><p style='color:#00ff88;font-size:20px'>🤖 IA: 45% Fan Zhendong VALUE +12%</p></div>
    <div class='card'><h2>Sun Yingsha vs Wang Manyu</h2><p style='color:#00ff88;font-size:20px'>🤖 IA: 64% Sun Yingsha VALUE +18%</p></div>
    <a class='btn' href='/test-bot'>🚨 PROBAR BOT TELEGRAM AHORA</a>
    <p style='text-align:center;color:#666'>Bot: @sportia_pro_v3_bot</p>
    </body></html>"""

@app.get("/test-bot")
def test_bot():
    msg = "🚨 <b>SPORTIA PRO V4 - ALERTA VALUE</b> 🚨\n\n🏓 Sun Yingsha vs Wang Manyu\n🤖 IA 64% VALUE +18%\n\n¡Bot funcionando Fernando! 🔥\nApp: https://web-production-a8499.up.railway.app"
    ok = send_telegram(msg)
    return HTMLResponse(f"<h1>{'✅ ENVIADO A TELEGRAM' if ok else '❌ ERROR'}</h1><p>Revisa @sportia_pro_v3_bot</p><a href='/'>Volver</a>")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
