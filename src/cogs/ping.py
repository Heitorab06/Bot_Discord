from discord.ext import commands
from discord import app_commands
import discord

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot
        
    @app_commands.command(name="ping", description="pong")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("pong")
    
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))