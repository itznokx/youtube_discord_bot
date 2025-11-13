import discord
import os
from dotenv import load_dotenv
load_dotenv()
application_token = os.getenv("DISCORD_TOKEN")

class DiscordClient (discord.Client):
    async def on_ready(self):
        printf(f'Logged on as {self.user}')
    async def on_message(self,message):
        printf(f'Message from {message.author}:{message.content}')
intents = discord.Intents.default()
intents.message_content = True
bot = DiscordClient(intents=intents)
bot.run(application_token)
