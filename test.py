import requests
from datetime import datetime, timedelta
import os

now = datetime.utcnow()
later = now + timedelta(hours=24)

username, api_key = os.getenv("CLIST_API_KEY").split(":")

params = {
    "username": username,
    "api_key": api_key,
    "start__gt": now.isoformat(),
    "start__lt": later.isoformat(),
    "order_by": "start",
    "limit": 20
}

r = requests.get("https://clist.by/api/v4/contest/", params=params)
print(r.status_code)
print(r.json())
