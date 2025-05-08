# Discord Music Bot

A Discord bot that can play music from YouTube and Spotify links, with ad-handling capabilities.

## Prerequisites

1. Python 3.8 or higher
2. A Discord bot token (get it from [Discord Developer Portal](https://discord.com/developers/applications))
3. Lavalink server (for music playback)

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory with your Discord bot token:
```
DISCORD_TOKEN=your_discord_bot_token_here
```

3. Set up Lavalink server:
   - Download the latest Lavalink.jar from [GitHub](https://github.com/freyacodes/Lavalink/releases)
   - Create an `application.yml` file with the following content:
   ```yaml
   server:
     port: 2333
     address: 127.0.0.1
   lavalink:
     server:
       password: "youshallnotpass"
       sources:
         youtube: true
         spotify: true
   ```
   - Run Lavalink server:
   ```bash
   java -jar Lavalink.jar
   ```

4. Run the bot:
```bash
python main.py
```

## Commands

- `!join` - Bot joins your voice channel
- `!play <url or search query>` - Play a song from YouTube or Spotify
- `!stop` - Stop playback and disconnect
- `!skip` - Skip the current song

## Features

- Play music from YouTube and Spotify links
- Search functionality for both platforms
- Ad handling (automatically skips ads)
- Basic playback controls (play, stop, skip) 