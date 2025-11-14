import discord
import os
import commands
from dotenv import load_dotenv
load_dotenv()
application_token = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
class DiscordClient (discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
    async def on_message(self,message):
        print(f'Message from {message.author}:{message.content}')
        res = commands.check_command(message)
        if res:
            await message.channel.send(res)
bot = DiscordClient(intents=intents)
bot.run(application_token)

