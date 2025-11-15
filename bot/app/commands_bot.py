import random
import sys
import discord
from discord import app_commands
from discord.ext import commands

class BotCommands (commands.Cog):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot
    @app_commands.command(
            name="rollnumbers",
            description="Rolls a number (random) between a interval of 2 values", 
)
    async def rollnumbers (self, interaction: discord.Interaction, floor:int, ceil:int):
        try:
            x = 0 if floor < 0 else floor
            y = sys.maxsize-1 if ceil > sys.maxsize else ceil
            await interaction.response.send_message(str(random.randint(x,y)))
        except Exception as e:
            print(f"ERRO NA RESPOSTA DA INTERACTION {e}")

async def setup(bot:commands.Bot):
    await bot.add_cog(BotCommands(bot))

""" Interaction json return
{'type': 1, 'options': [{'value': 1, 'type': 4, 'name': 'floor'}, {'value': 10, 'type': 4, 'name': 'ceil'}], 'name': 'rollnumbers', 'id': '1439078704553922723', 'guild_id': '76161895154502861
8'}
"""
