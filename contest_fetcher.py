import aiohttp
from datetime import datetime, timedelta
import pytz
from config import CLIST_API_KEY

async def get_upcoming_contests():
    url = "https://clist.by/api/v4/contest/"
    now = datetime.utcnow()
    later = now + timedelta(hours=24)

    params = {
        "username": CLIST_API_KEY.split(":")[0],
        "api_key": CLIST_API_KEY.split(":")[1],
        "start__gt": now.isoformat(),
        "start__lt": later.isoformat(),
        "order_by": "start",
        "limit": 20,
    }

    headers = {
        "Accept": "application/json",
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as resp:
            data = await resp.json()

    contests = data.get("objects", [])
    ist = pytz.timezone("Asia/Kolkata")

    for c in contests:
        start_utc = datetime.fromisoformat(c["start"]).replace(tzinfo=pytz.UTC)
        end_utc = datetime.fromisoformat(c["end"]).replace(tzinfo=pytz.UTC)

        start_ist = start_utc.astimezone(ist)
        end_ist = end_utc.astimezone(ist)

        c["start_ist"] = start_ist.strftime("%d %b %Y, %I:%M %p IST")
        c["end_ist"] = end_ist.strftime("%d %b %Y, %I:%M %p IST")

        duration_seconds = int(c["duration"])
        hours, remainder = divmod(duration_seconds, 3600)
        minutes = remainder // 60
        c["duration_fmt"] = f"{hours}h {minutes}m"
    
    return contests






# import aiohttp
# from datetime import datetime, timedelta
# import pytz
# from config import CLIST_API_KEY

# async def get_upcoming_contests(platform_filter=None):
#     url = "https://clist.by/api/v4/contest/"
#     now = datetime.utcnow()
#     later = now + timedelta(days=7)

#     params = {
#         "username": CLIST_API_KEY.split(":")[0],
#         "api_key": CLIST_API_KEY.split(":")[1],
#         "start__gt": now.isoformat(),
#         "start__lt": later.isoformat(),
#         "order_by": "start",
#         "limit": 100,
#     }

#     headers = {"Accept": "application/json"}

#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, headers=headers, params=params) as resp:
#             data = await resp.json()

#     contests = data.get("objects", [])
#     ist = pytz.timezone("Asia/Kolkata")

#     filtered = []
#     platform_set = set()

#     for c in contests:
#         platform_id = c["resource"].lower()
#         platform_set.add(platform_id)

#         if platform_filter and platform_filter.lower() != platform_id:
#             continue

#         start_utc = datetime.fromisoformat(c["start"]).replace(tzinfo=pytz.UTC)
#         end_utc = datetime.fromisoformat(c["end"]).replace(tzinfo=pytz.UTC)

#         start_ist = start_utc.astimezone(ist)
#         end_ist = end_utc.astimezone(ist)

#         c["start_ist"] = start_ist.strftime("%d %b %Y, %I:%M %p IST")
#         c["end_ist"] = end_ist.strftime("%d %b %Y, %I:%M %p IST")

#         duration_seconds = int(c["duration"])
#         hours, remainder = divmod(duration_seconds, 3600)
#         minutes = remainder // 60
#         c["duration_fmt"] = f"{hours}h {minutes}m"

#         filtered.append(c)

#     return filtered, sorted(platform_set)
