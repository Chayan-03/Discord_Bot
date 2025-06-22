from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CLIST_API_KEY = os.getenv("CLIST_API_KEY")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
