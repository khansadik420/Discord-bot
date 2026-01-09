import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True  # important

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

token = os.getenv("TOKEN")

if not token:
    raise ValueError("TOKEN environment variable not set")

bot.run(token)
