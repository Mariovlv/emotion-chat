from twitchio.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

# Variables
streamer = ''

bot = commands.Bot (
    token = os.getenv('TOKEN'),
    client_id = os.getenv('CLIENT_ID'),
    nick = 'Ponchito',
    prefix = '!',
    initial_channels = [streamer]
)

@bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == streamer:
        print('Received...', ctx.content)

    if ctx.content.lower() == 'ping':
        await ctx.channel.send('pong')

if __name__ == '__main__':
    bot.run()