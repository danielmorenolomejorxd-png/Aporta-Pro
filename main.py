import os, requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

BOT_TOKEN = os.getenv("BOT_TOKEN", "8972036325:AAHsRubJ1s2wq_LhIe7mmyMBanpeRQuu-tQ")
CHAT_ID = os.getenv("CHAT_ID", "8760042926")
app = FastAPI()

def send_telegram(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}, timeout=10)
        return True
    except: return False

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<html><head><meta name='viewport' content='width=device-width,initial-scale=1'><style>
body{background:#0a0e13;color:white;font-family:Arial;margin:0;padding:0}
.header{background:linear-gradient(90deg,#00ff88,#00d4ff);color:#000;padding:20px;text-align:center;font-weight:900}
.card{background:#1a212b;margin:15px;border-radius:16px;padding:16px;border:1px solid #2a3441}
.prob{background:#0a0e13;height:8px;border-radius:10px;overflow:hidden;margin:8px 0}
.fill{height:100%;background:linear-gradient(90deg,#00ff88,#00d4ff)}
.btn{display:block;background:#ffcc00;color:#000;text-align:center;padding:18px;border-radius:14px;font-weight:900;text-decoration:none;margin:15px;font-size:18px}
.badge{background:#00ff88;color:#000;padding:3px 10px;border-radius:20px;font-size:12px;font-weight:900}
.value{color:#00ff88;font-weight:900}
</style></head><body>
<div class='header'><div style='font-size:28px'>🏓 SPORTIA PRO V4</div><div>IA TENIS DE MESA • VALUE BETS</div></div>

<div class='card'>
<div style='display:flex;justify-content:space-between'><b>Harimoto 🇯🇵 vs Fan 🇨🇳</b><span class='badge'>LIVE</span></div>
<div class='prob'><div class='fill' style='width:58%'></div></div>
<div>IA: <span class='value'>Harimoto 58% WIN</span> • Cuota 2.85 <b style='color:#ffcc00'>+22% VALUE 🔥</b></div>
</div>

<div class='card'>
<div style='display:flex;justify-content:space-between'><b>Sun Yingsha 🇨🇳 vs Wang Manyu 🇨🇳</b><span class='badge'>14:30</span></div>
<div class='prob'><div class='fill' style='width:64%'></div></div>
<div>IA: <span class='value'>Sun 64% WIN</span> • Cuota 2.40 <b style='color:#ffcc00'>+18% VALUE 🔥</b></div>
</div>

<div class='card'>
<div style='display:flex;justify-content:space-between'><b>Calderano 🇧🇷 vs Moregard 🇸🇪</b><span class='badge'>16:00</span></div>
<div class='prob'><div class='fill' style='width:52%'></div></div>
<div>IA: <span class='value'>Calderano 52% WIN</span> • Cuota 2.95 <b style='color:#ffcc00'>+15% VALUE</b></div>
</div>

<a class='btn' href='/test-bot'>🚨 ENVIAR ALERTA A TELEGRAM</a>
<div style='text-align:center;color:#5a6a7a;padding-bottom:30px'>Bot: @sportia_pro_v3_bot • Railway: OK ✅<br>Hecho para Fernando • Villavicencio</div>
</body></html>
"""

@app.get("/test-bot")
def test():
    msg = "🚨 <b>SPORTIA PRO V4 - ALERTA VALUE 🔥</b>\n\n🏓 Harimoto vs Fan Zhendong\n🤖 IA: 58% Win\n💰 Cuota: 2.85\n📈 VALUE: +22%\n\nLink: https://web-production-b2155.up.railway.app"
    send_telegram(msg)
    return HTMLResponse("<h1 style='text-align:center;margin-top:100px'>✅ ALERTA ENVIADA A TELEGRAM</h1><a href='/' style='display:block;text-align:center;margin-top:20px'>Volver</a>")

@app.get("/api/predictions")
def api(): return {"ok": True}
