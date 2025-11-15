import discord
import os
import asyncio
import discord
from discord.ext import commands
from aiohttp import ClientSession
from dotenv import load_dotenv
load_dotenv()

class DiscordBot (commands.Bot):
    def __init__(
        self,
        *args,
        initial_extensions: list[str],
        web_client: ClientSession,
        testing_guild_id,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.web_client = web_client
        self.testing_guild_id = testing_guild_id
        self.initial_extensions = initial_extensions
    async def on_ready (self):
        print(f'Logged on as {self.user}')
    async def setup_hook(self) -> None:
        for extension in self.initial_extensions:
            try:
                await self.load_extension(extension)
                print(f"Extensao {extension} carregada")
            except Exception as e:
                print(f"Erro {e}")
        if self.testing_guild_id:
            print(f"ID_SERVER: {self.testing_guild_id}")
            try:
                guild = discord.Object(self.testing_guild_id)
                self.tree.copy_global_to(guild=guild)
                await self.tree.sync(guild=guild)
                print("Comandos Sincronizados")
            except Exception as e:
                print(f"Erro {e}, comandos não sincronizados")
        else:
            print("ID do servidor None")

async def start_bot ():
    async with ClientSession() as session:
        bot_commands = ['commands_bot']
        intents = discord.Intents.default()
        intents.message_content = True
        async with DiscordBot (
                commands.when_mentioned,
                web_client = session,
                testing_guild_id = os.getenv("SERVER_ID"),
                initial_extensions = bot_commands,
                intents=intents
        ) as bot:
            await bot.start(os.getenv("DISCORD_TOKEN"))
asyncio.run(start_bot())

