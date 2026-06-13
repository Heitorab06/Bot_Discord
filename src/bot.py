from discord.ext import commands
import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")

@bot.command()
async def ping(ctx:commands.Context):
    await ctx.send("pong")
    
@bot.command()
async def sortear(ctx:commands.Context, n1:int, n2:int):
    await ctx.reply(random.randint(n1, n2))

bot.run(TOKEN)