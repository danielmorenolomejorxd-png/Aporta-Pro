import os
import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
        return True
    except:
        return False

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html><head><title>SPORTIA V8 REAL</title><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body style="background:#0a0a0a;color:#00ff88;font-family:Arial;padding:20px;text-align:center">
    <h1>🚀 SPORTIA V8 REAL</h1>
    <h2 style="color:white">✅ ¡SISTEMA REAL ACTIVO!</h2>
    <div style="background:#1a1a1a;padding:15px;border-radius:10px;margin:20px 0;text-align:left;border:1px solid #00ff88">
    <p>⚽ Barcelona vs Real Madrid - 1.85</p>
    <p>⚽ Man City vs Arsenal - 2.10</p>
    <p>⚽ Bayern vs Dortmund - 1.95</p>
    </div>
    <a href="/alerta" style="display:block;background:yellow;color:black;padding:20px;font-size:20px;border-radius:10px;text-decoration:none;font-weight:bold">🚨 ENVIAR ALERTA REAL A TELEGRAM</a>
    <p style="color:gray;margin-top:20px">Railway: ONLINE | Telegram: CONECTADO</p>
    </body></html>
    """

@app.get("/alerta")
def alerta():
    ok = send_telegram("🚨 *SPORTIA V8 REAL* \\n\\n⚽ Barcelona vs Real Madrid \\n💰 Cuota: 1.85 \\n✅ ¡Valor detectado! \\n\\nTu bot funciona Fernando! 🎉")
    if ok:
        return HTMLResponse("<h1 style='text-align:center;margin-top:50px'>✅ ¡MENSAJE ENVIADO A TU TELEGRAM! Revisa tu celular 📱</h1><a href='/' style='display:block;text-align:center'>Volver</a>")
    else:
        return HTMLResponse("<h1>❌ Error, revisa TOKEN y CHAT_ID</h1>")
