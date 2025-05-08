import discord
from discord.ext import commands
import wavelink
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')
    # Initialize wavelink
    node = wavelink.Node(
        uri='http://localhost:2333',  # Lavalink server address
        password='youshallnotpass'    # Lavalink server password
    )
    await wavelink.NodePool.connect(client=bot, nodes=[node])

@bot.command(name='join')
async def join(ctx):
    """Join the user's voice channel"""
    if not ctx.author.voice:
        return await ctx.send("You need to be in a voice channel first!")
    
    channel = ctx.author.voice.channel
    await channel.connect(cls=wavelink.Player)
    await ctx.send(f"Joined {channel.name}")

@bot.command(name='play')
async def play(ctx, *, query: str):
    """Play a song from YouTube or Spotify"""
    if not ctx.voice_client:
        if not ctx.author.voice:
            return await ctx.send("You need to be in a voice channel first!")
        await ctx.author.voice.channel.connect(cls=wavelink.Player)
    
    player = ctx.voice_client

    # Search for the track
    tracks = await wavelink.NodePool.get_node().get_tracks(query)
    
    if not tracks:
        return await ctx.send("No tracks found!")
    
    track = tracks[0]
    
    # Play the track
    await player.play(track)
    await ctx.send(f"Now playing: {track.title}")

@bot.command(name='stop')
async def stop(ctx):
    """Stop the current playback"""
    if not ctx.voice_client:
        return await ctx.send("I'm not playing anything!")
    
    player = ctx.voice_client
    await player.disconnect()
    await ctx.send("Stopped playback and disconnected")

@bot.command(name='skip')
async def skip(ctx):
    """Skip the current song"""
    if not ctx.voice_client:
        return await ctx.send("I'm not playing anything!")
    
    player = ctx.voice_client
    await player.stop()
    await ctx.send("Skipped the current song")

# Run the bot
if __name__ == "__main__":
    asyncio.run(bot.run(os.getenv('DISCORD_TOKEN')))
