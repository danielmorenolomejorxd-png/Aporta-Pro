import os, requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

BOT_TOKEN = os.getenv("BOT_TOKEN", "8972036325:AAHsRubJ1s2wq_LhIe7mmyMBanpeRQuu-tQ")
CHAT_ID = os.getenv("CHAT_ID", "8760042926")
app = FastAPI()

def send(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}, timeout=10)
    except: pass

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<html><head><meta name='viewport' content='width=device-width,initial-scale=1'><style>
body{background:#0a0e13;color:#fff;font-family:Arial;margin:0}
.head{background:linear-gradient(90deg,#00ff88,#00d4ff);color:#000;padding:18px;text-align:center;font-weight:900;font-size:22px}
.tabs{display:flex;gap:8px;padding:12px;overflow-x:auto;position:sticky;top:0;background:#0a0e13;z-index:10}
.tab{background:#1a212b;border:1px solid #2a3441;padding:8px 14px;border-radius:20px;font-weight:700;cursor:pointer;white-space:nowrap}
.tab.active{background:#ffcc00;color:#000;border-color:#ffcc00}
.card{background:#1a212b;margin:10px 15px;border-radius:14px;padding:14px;border:1px solid #2a3441}
.bar{background:#0a0e13;height:7px;border-radius:10px;margin:6px 0}
.fill{height:100%;background:linear-gradient(90deg,#00ff88,#00d4ff)}
.btn{display:block;background:#ffcc00;color:#000;text-align:center;padding:16px;border-radius:12px;font-weight:900;text-decoration:none;margin:15px}
.sport{font-size:12px;color:#8a9aaa}
.hidden{display:none}
</style>
<script>
function filter(s){
 document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
 document.getElementById('tab-'+s).classList.add('active');
 document.querySelectorAll('.card').forEach(c=>{
   if(s=='all' || c.dataset.sport==s) c.classList.remove('hidden');
   else c.classList.add('hidden');
 });
}
</script></head><body>
<div class='head'>🏆 SPORTIA PRO V6</div>

<div class='tabs'>
<div id='tab-all' class='tab active' onclick="filter('all')">🔥 Todos</div>
<div id='tab-futbol' class='tab' onclick="filter('futbol')">⚽ Fútbol</div>
<div id='tab-pingpong' class='tab' onclick="filter('pingpong')">🏓 Ping Pong</div>
<div id='tab-tenis' class='tab' onclick="filter('tenis')">🎾 Tenis</div>
<div id='tab-basket' class='tab' onclick="filter('basket')">🏀 Basket</div>
</div>

<div class='card' data-sport='futbol'>
<span class='sport'>⚽ FÚTBOL • LaLiga • 15:00</span><br>
<b>Real Madrid vs Barcelona</b> <span style='background:#ff4444;color:#fff;padding:2px 8px;border-radius:10px;font-size:11px'>LIVE 🔥</span>
<div class='bar'><div class='fill' style='width:62%'></div></div>
IA: <b style='color:#00ff88'>Madrid 62% WIN</b> • Cuota 2.10 <b style='color:#ffcc00'>+24% VALUE</b>
</div>

<div class='card' data-sport='pingpong'>
<span class='sport'>🏓 TENIS DE MESA • WTT • 14:30</span><br>
<b>Harimoto 🇯🇵 vs Fan 🇨🇳</b> <span style='background:#00ff88;color:#000;padding:2px 8px;border-radius:10px;font-size:11px'>VALUE</span>
<div class='bar'><div class='fill' style='width:58%'></div></div>
IA: <b style='color:#00ff88'>Harimoto 58%</b> • Cuota 2.85 <b style='color:#ffcc00'>+22% VALUE</b>
</div>

<div class='card' data-sport='tenis'>
<span class='sport'>🎾 TENIS ATP • US Open • 16:00</span><br>
<b>Alcaraz vs Sinner</b>
<div class='bar'><div class='fill' style='width:55%'></div></div>
IA: <b style='color:#00ff88'>Alcaraz 55%</b> • Cuota 2.20 <b style='color:#ffcc00'>+18% VALUE</b>
</div>

<div class='card' data-sport='basket'>
<span class='sport'>🏀 NBA • Pretemporada • 19:00</span><br>
<b>Lakers vs Warriors</b>
<div class='bar'><div class='fill' style='width:60%'></div></div>
IA: <b style='color:#00ff88'>Lakers 60%</b> • Cuota 1.95 <b style='color:#ffcc00'>+16% VALUE</b>
</div>

<div class='card' data-sport='futbol'>
<span class='sport'>⚽ FÚTBOL • Premier • 13:30</span><br>
<b>Man City vs Arsenal</b>
<div class='bar'><div class='fill' style='width:54%'></div></div>
IA: <b style='color:#00ff88'>City 54%</b> • Cuota 2.30 <b style='color:#ffcc00'>+12% VALUE</b>
</div>

<div class='card' data-sport='pingpong'>
<span class='sport'>🏓 TENIS DE MESA • WTT • 18:00</span><br>
<b>Calderano 🇧🇷 vs Moregard 🇸🇪</b>
<div class='bar'><div class='fill' style='width:52%'></div></div>
IA: <b style='color:#00ff88'>Calderano 52%</b> • Cuota 2.95 <b style='color:#ffcc00'>+15% VALUE</b>
</div>

<a class='btn' href='/test-bot'>🚨 ENVIAR ALERTA A TELEGRAM</a>
<div style='text-align:center;color:#5a6a7a;padding:0 15px 25px;font-size:13px'>V6 con filtros funcionando • Bot: @sportia_pro_v3_bot</div>
</body></html>
"""

@app.get("/test-bot")
def test():
    send("🚨 <b>SPORTIA V6</b>\n\nFiltro Ping Pong funciona!\n\n🏓 Harimoto 58% +22% VALUE")
    return HTMLResponse("<h1 style='text-align:center;margin-top:80px'>✅ ENVIADO</h1><a href='/' style='display:block;text-align:center'>Volver</a>")
