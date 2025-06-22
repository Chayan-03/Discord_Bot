import os
from dotenv import load_dotenv

load_dotenv()

print("DISCORD_TOKEN:", os.getenv("DISCORD_TOKEN"))
print("CLIST_API_KEY:", os.getenv("CLIST_API_KEY"))
