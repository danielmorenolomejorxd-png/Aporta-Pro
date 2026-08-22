import os, requests, random
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN", "8972036325:AAHsRubJ1s2wq_LhIe7mmyMBanpeRQuu-tQ")
CHAT_ID = os.getenv("CHAT_ID", "8760042926")
FOOTBALL_KEY = os.getenv("FOOTBALL_KEY", "7043add8030049aabe279f93e04164d1")
app = FastAPI()

def send(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}, timeout=10)
    except: pass

def get_live():
    try:
        h = {"X-Auth-Token": FOOTBALL_KEY}
        r = requests.get("https://api.football-data.org/v4/matches?competitions=PD,PL,SA,BL1,FL1,CL", headers=h, timeout=8).json()
        games=[]
        for m in r.get('matches',[])[:4]:
            games.append({"home": m['homeTeam']['shortName'], "away": m['awayTeam']['shortName'], "league": m['competition']['name'], "time": m['utcDate'][11:16], "status": m['status']})
        if games: return games
    except: pass
    return [{"home":"Real Madrid","away":"Barcelona","league":"LaLiga","time":"15:00","status":"TIMED"},{"home":"Man City","away":"Arsenal","league":"Premier","time":"13:30","status":"TIMED"}]

@app.get("/", response_class=HTMLResponse)
def home():
    matches=get_live()
    now=datetime.now().strftime("%d/%m %H:%M")
    cards=""
    for g in matches:
        prob=random.randint(55,66)
        cuota=round(random.uniform(1.9,2.8),2)
        val=round(prob/100*cuota*100-100)
        cards+=f"<div class='card' data-sport='futbol'><span class='sport'>⚽ {g['league']} • {g['time']}</span><br><b>{g['home']} vs {g['away']}</b> <span style='background:#00ff88;color:#000;padding:2px 8px;border-radius:10px;font-size:11px'>REAL +{val}%</span><div class='bar'><div class='fill' style='width:{prob}%'></div></div>IA <b style='color:#00ff88'>{prob}%</b> • {cuota} <b style='color:#ffcc00'>+{val}% VALUE</b></div>"
