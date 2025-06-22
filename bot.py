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


#
#
# import discord
# from discord.ext import tasks, commands
# import asyncio
# from contest_fetcher import get_upcoming_contests
# from config import DISCORD_TOKEN, CHANNEL_ID
#
# intents = discord.Intents.default()
# bot = commands.Bot(command_prefix="!", intents=intents)
#
# @bot.event
# async def on_ready():
#     print(f"✅ Bot is online as {bot.user}")
#     post_daily_contests.start()
#
# @tasks.loop(hours=6)
# async def post_daily_contests():
#     channel = bot.get_channel(CHANNEL_ID)
#     contests = await get_upcoming_contests()
#
#     if not contests:
#         await channel.send("❌ No upcoming contests found in the next 24 hours.")
#         return
#
#     await channel.send("📢 **Upcoming Competitive Programming Contests (next 24h):**")
#
#     for contest in contests:
#         name = contest["event"]
#         platform = contest["resource"].capitalize()
#         start = contest["start_ist"]
#         end = contest["end_ist"]
#         duration = contest["duration_fmt"]
#         link = contest["href"]
#
#         embed = discord.Embed(
#             title=f"🧑‍💻 {name}",
#             url=link,
#             description=(
#                 f"🌐 **Platform:** {platform}\n"
#                 f"📅 **Start:** {start}\n"
#                 f"🏁 **End:** {end}\n"
#                 f"⏱️ **Duration:** {duration}\n"
#                 f"🔗 [**Click here to register**]({link})"
#             ),
#             color=discord.Color.blue()
#         )
#         await channel.send(embed=embed)
#
# bot.run(DISCORD_TOKEN)
# # import discord
# # from discord.ext import commands
# # from contest_fetcher import get_upcoming_contests
# # from config import DISCORD_TOKEN, CHANNEL_ID
# #
# # intents = discord.Intents.default()
# # bot = commands.Bot(command_prefix="!", intents=intents)
# # PLATFORM_CACHE = []
# #
# # @bot.event
# # async def on_ready():
# #     print(f"✅ Bot is online as {bot.user}")
# #
# # @bot.command(name="platforms")
# # async def platforms(ctx):
# #     _, platforms = await get_upcoming_contests()
# #     global PLATFORM_CACHE
# #     PLATFORM_CACHE = platforms
# #
# #     msg = "**Supported Platforms & Commands:**\n"
# #     for p in platforms:
# #         msg += f"🔹 `!{p}`\n"
# #     await ctx.send(msg)
# #
# # @bot.command(name="allcontests")
# # async def allcontests(ctx):
# #     contests, _ = await get_upcoming_contests()
# #     await send_contests(ctx, contests, "All Platforms")
# #
# # @bot.event
# # async def on_message(message):
# #     if message.author.bot:
# #         return
# #
# #     content = message.content.lower()
# #     if content.startswith("!"):
# #         cmd = content[1:]
# #         contests, platforms = await get_upcoming_contests(platform_filter=cmd)
# #
# #         if contests:
# #             await send_contests(message.channel, contests, cmd)
# #         elif cmd == "platforms" or cmd == "allcontests":
# #             await bot.process_commands(message)
# #         else:
# #             await message.channel.send(f"❌ No contests found or invalid platform: `{cmd}`.\nUse `!platforms` to see all available options.")
# #
# # async def send_contests(ctx, contests, platform_label):
# #     if not contests:
# #         await ctx.send(f"❌ No upcoming contests found for **{platform_label}**.")
# #         return
# #
# #     await ctx.send(f"📢 **Upcoming Contests ({platform_label}):**")
# #
# #     for contest in contests:
# #         name = contest["event"]
# #         platform = contest["resource"].capitalize()
# #         start = contest["start_ist"]
# #         end = contest["end_ist"]
# #         duration = contest["duration_fmt"]
# #         link = contest["href"]
# #
# #         embed = discord.Embed(
# #             title=f"🧑‍💻 {name}",
# #             url=link,
# #             description=(
# #                 f"🌐 **Platform:** {platform}\n"
# #                 f"📅 **Start:** {start}\n"
# #                 f"🏁 **End:** {end}\n"
# #                 f"⏱️ **Duration:** {duration}\n"
# #                 f"🔗 [**Register Here**]({link})"
# #             ),
# #             color=discord.Color.purple()
# #         )
# #         await ctx.send(embed=embed)
# #
# # bot.run(DISCORD_TOKEN)




