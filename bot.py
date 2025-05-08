import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True  # Enable voice state intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('Bot is ready!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def join(ctx):
    if not ctx.author.voice:
        return await ctx.send("You need to be in a voice channel!")
    
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Joined {channel.name}")
    except Exception as e:
        print(f"Error joining voice channel: {str(e)}")
        await ctx.send(f"Failed to join voice channel: {str(e)}")

@bot.command()
async def leave(ctx):
    if not ctx.voice_client:
        return await ctx.send("I'm not in a voice channel!")
    
    await ctx.voice_client.disconnect()
    await ctx.send("Left the voice channel!")

# Run the bot
bot.run(os.getenv('DISCORD_TOKEN')) 