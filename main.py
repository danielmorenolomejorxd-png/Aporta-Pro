import os, requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

BOT_TOKEN = os.getenv("BOT_TOKEN", "8972036325:AAHsRubJ1s2wq_LhIe7mmyMBanpeRQuu-tQ")
CHAT_ID = os.getenv("CHAT_ID", "8760042926")
app = FastAPI()

def send_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": CHAT_ID, "text": msg}, timeout=10)
        return True
    except:
        return False

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html><body style='background:#000;color:#fff;font-family:Arial;padding:20px;text-align:center'>
    <h1>🏓 SportIA Pro V4 BOT ACTIVO</h1>
    <p style='color:#0f0'>Online ✅</p>
    <a href='/test-bot' style='background:yellow;color:black;padding:20px;display:block;border-radius:10px;font-weight:bold;text-decoration:none;margin:20px 0'>🚨 PROBAR BOT TELEGRAM AHORA</a>
    <p>Bot: @sportia_pro_v3_bot</p>
    </body></html>
    """

@app.get("/test-bot")
def test_bot():
    ok = send_telegram("🚨 SPORTIA PRO V4 FUNCIONA FERNANDO 🔥 Tu bot ya esta activo!")
    return HTMLResponse(f"<h1>{'✅ ENVIADO' if ok else '❌ ERROR'}</h1><a href='/'>Volver</a>")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
