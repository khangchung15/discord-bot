import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import yt_dlp
import asyncio
import subprocess

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Configure yt-dlp options
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

# Update this path to where your ffmpeg.exe is located
FFMPEG_PATH = r"C:\Users\khang\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"

ffmpeg_options = {
    'options': '-vn',
    'executable': FFMPEG_PATH
}

ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        try:
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
            
            if data is None:
                raise Exception("Could not extract video information")

            if 'entries' in data:
                # take first item from a playlist
                data = data['entries'][0]

            filename = data['url'] if stream else ytdl.prepare_filename(data)
            return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)
        except Exception as e:
            print(f"Error in from_url: {str(e)}")
            raise

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('Bot is ready!')
    
    # Check if FFmpeg is installed
    try:
        if os.path.exists(FFMPEG_PATH):
            print(f"FFmpeg found at: {FFMPEG_PATH}")
        else:
            print(f"WARNING: FFmpeg not found at: {FFMPEG_PATH}")
            print("Please update the FFMPEG_PATH in the code to point to your ffmpeg.exe")
    except Exception as e:
        print(f"Error checking FFmpeg: {str(e)}")

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

@bot.command()
async def play(ctx, *, url):
    if not ctx.voice_client:
        if not ctx.author.voice:
            return await ctx.send("You need to be in a voice channel!")
        await ctx.author.voice.channel.connect()
    
    try:
        async with ctx.typing():
            # If the input is not a URL, treat it as a search query
            if not url.startswith(('http://', 'https://')):
                url = f"ytsearch:{url}"
            
            player = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
            await ctx.send(f'Now playing: {player.title}')
    except Exception as e:
        error_msg = str(e)
        print(f"Error playing music: {error_msg}")
        if "ffmpeg was not found" in error_msg.lower():
            await ctx.send(f"Error: FFmpeg not found at {FFMPEG_PATH}. Please update the FFMPEG_PATH in the code.")
        else:
            await ctx.send(f"Error playing music: {error_msg}")

@bot.command()
async def stop(ctx):
    if not ctx.voice_client:
        return await ctx.send("I'm not playing anything!")
    
    ctx.voice_client.stop()
    await ctx.send("Stopped playing!")

@bot.command()
async def pause(ctx):
    if not ctx.voice_client:
        return await ctx.send("I'm not playing anything!")
    
    if ctx.voice_client.is_paused():
        return await ctx.send("Already paused!")
    
    ctx.voice_client.pause()
    await ctx.send("Paused!")

@bot.command()
async def resume(ctx):
    if not ctx.voice_client:
        return await ctx.send("I'm not playing anything!")
    
    if not ctx.voice_client.is_paused():
        return await ctx.send("Not paused!")
    
    ctx.voice_client.resume()
    await ctx.send("Resumed!")

# Run the bot
bot.run(os.getenv('DISCORD_TOKEN'))