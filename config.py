# DISCORD_TOKEN ="MTM4NjAyNTMxMTcyMzk4MzAwOA.G_3v5L.bvKWG4jV4ORw9ZWNk9StuzSk7DHN2LD8I-BlA8"
# CHANNEL_ID = 1386024145342697475  # Replace with your actual #contest-updates channel ID as an integer
# CLIST_API_KEY ="Explorer_the_gr8:bda0f0a94f3edef50553e20a2841033001b277f6"


from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CLIST_API_KEY = os.getenv("CLIST_API_KEY")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

