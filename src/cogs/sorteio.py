from discord.ext import commands
from discord import app_commands
import discord
from random import randint

class Sorteio(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot
        
    @app_commands.command(name="sortear", description="Sorteia um número no intervalo")
    @app_commands.describe(inicio="Valor Mínimo", fim="Valor Máximo")
    async def sortear(self, interaction: discord.Interaction, inicio:int, fim:int):
        await interaction.response.send_message(f"🎲 O valor sorteado foi: {randint(inicio, fim)} 🎲")
        
async def setup(bot: commands.Bot):
    print("Carregando cog sorteio")
    await bot.add_cog(Sorteio(bot))