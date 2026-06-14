from discord.ext import commands
import discord
import os
import random
import asyncio
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
    
    synced = await bot.tree.sync()
    print(f"Logado como {bot.user}")
    print(f"{len(synced)} comandos sincronizados")
    
    for c in bot.tree.get_commands():
        print(c.name)


async def main():
    async with bot:
        
        await bot.load_extension("cogs.sorteio")
        await bot.load_extension("cogs.ping")
        
        await bot.start(TOKEN)
    
    
asyncio.run(main())

