# Discord Music Bot

Discord bot that can play music in voice channels using YouTube links or search queries.

## Features

- Play music from YouTube links or search queries
- Music controls (play, pause, resume, stop)
- Simple command interface

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- FFmpeg
- pip (Python package installer)

## Installation

1. **Clone repo**
   ```
   git clone https://github.com/khangchung15/discord-bot.git
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg**
   - Download FFmpeg from https://www.gyan.dev/ffmpeg/builds/
   - Choose the "essentials" build
   - Extract the zip file
   - Add the `bin` folder to your system PATH
   - For Windows:
     1. Open System Properties > Advanced > Environment Variables
     2. Under System Variables, find and select "Path"
     3. Click "Edit"
     4. Click "New"
     5. Add the path to the `bin` folder (e.g., `C:\ffmpeg\bin` or in `Downloads\ffmpeg\bin`)
     6. Click "OK" on all windows
   - For Mac: Not sure, never used it before

4. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add your Discord bot token:
     ```
     DISCORD_TOKEN=your_bot_token_here
     ```
   - To get bot token, go to: https://discord.com/developers/
   - Sign up or Log in account
   
   - Invite Bot To Server:
      1. New Application > Make a new bot
      2. In OAuth2 tab on the left > under "OAuth2 URL Generator", check "bot" > scroll down more > check appropriate permission (I had Administrator for testing)
      3. Under "Generated URL" copy & paste into new tab to invite the bot to server
   - Get Discord Bot Token:
    1. Go into Bot tab on the left > under "Token", click "Reset Token" > copy that new token and paste in `.env` file
    

## Configuration

**Update FFmpeg Path**
   - Open `bot.py`
   - Find the `FFMPEG_PATH` variable
   - Update it to point to your FFmpeg executable:
     ```python
     FFMPEG_PATH = r"C:\Users\username\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"
     ```
   - Exact path will be different depends on the version of FFMPEG you downloaded

## Running the Bot

**Local Development**
   Run `python bot.py` and `java -jar Lavalink.jar` on terminal

## Commands

- `!ping` - Check if the bot is responsive
- `!join` - Bot joins your current voice channel
- `!leave` - Bot leaves the voice channel
- `!play <song name or URL>` - Play a song
- `!pause` - Pause the current song
- `!resume` - Resume the paused song
- `!stop` - Stop playing and clear the queue

## License

This project is licensed under the MIT License - see the LICENSE file for details. 