import requests
from datetime import datetime
import random

def get_weather():
    try:
        city = "Delhi"
        url = f"https://wttr.in/{city}?format=3"
        return requests.get(url).text
    except:
        return "Weather unavailable"

def get_motivation():
    quotes = [
        "Discipline beats motivation.",
        "Small progress is still progress.",
        "Consistency creates success.",
        "Your future depends on what you do today."
    ]
    return random.choice(quotes)

def get_news():
    try:
        return "Top headline: Stay informed."
    except:
        return "News unavailable"

def daily_dashboard():
    today = datetime.now().strftime("%d %B %Y")

    dashboard = f"""
📊 DAILY INTELLIGENCE DASHBOARD

Date: {today}

🌤 Weather: {get_weather()}
📰 News: {get_news()}
💡 Motivation: {get_motivation()}
💊 Health Tip: Drink water and stretch.

"""
    return dashboard

