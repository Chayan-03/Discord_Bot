import discord
from discord.ext import tasks, commands
import asyncio
from contest_fetcher import get_upcoming_contests
from config import DISCORD_TOKEN, CHANNEL_ID

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")
    post_daily_contests.start()

@tasks.loop(hours=6)
async def post_daily_contests():
    channel = bot.get_channel(CHANNEL_ID)
    contests = await get_upcoming_contests()
    
    if not contests:
        await channel.send("❌ No upcoming contests found in the next 24 hours.")
        return

    await channel.send("📢 **Upcoming Competitive Programming Contests (next 24 hours):**")

    for contest in contests:
        name = contest["event"]
        platform = contest["resource"].upper()
        start = contest["start_ist"]
        end = contest["end_ist"]
        duration = contest["duration_fmt"]
        link = contest["href"]

        embed = discord.Embed(
            title=f"🎯 {name}",
            url=link,
            description=(
                f"🧩 **Platform:** `🟦 {platform}`\n\n"
                f"📅 **Start:** {start}\n"
                f"🏁 **End:** {end}\n"
                f"⏱️ **Duration:** {duration}\n"
                f"🔗 [**Click here to register**]({link})"
            ),
            color=discord.Color.blurple()  # You can use Color.red(), .green(), etc.
            
        )
        
        await channel.send(embed=embed)

bot.run(DISCORD_TOKEN)







