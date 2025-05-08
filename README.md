# Discord Music Bot

A Discord bot that can play music in voice channels using YouTube links or search queries.

## Features

- Play music from YouTube links or search queries
- Basic music controls (play, pause, resume, stop)
- Simple command interface
- Voice channel management

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- FFmpeg
- pip (Python package installer)

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd DiscordBot
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg**
   - Download FFmpeg from [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
   - Choose the "essentials" build
   - Extract the zip file
   - Add the `bin` folder to your system PATH
   - For Windows:
     1. Open System Properties > Advanced > Environment Variables
     2. Under System Variables, find and select "Path"
     3. Click "Edit"
     4. Click "New"
     5. Add the path to the `bin` folder (e.g., `C:\ffmpeg\bin`)
     6. Click "OK" on all windows

4. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add your Discord bot token:
     ```
     DISCORD_TOKEN=your_bot_token_here
     ```

## Configuration

1. **Update FFmpeg Path**
   - Open `bot.py`
   - Find the `FFMPEG_PATH` variable
   - Update it to point to your FFmpeg executable:
     ```python
     FFMPEG_PATH = r"C:\path\to\your\ffmpeg.exe"
     ```

## Running the Bot

1. **Local Development**
   ```bash
   python bot.py
   ```

2. **Deployment Options**
   The bot can be deployed to various platforms:

   ### Railway
   1. Create an account on [Railway](https://railway.app/)
   2. Create a new project
   3. Connect your GitHub repository
   4. Add environment variables (DISCORD_TOKEN)
   5. Deploy

   ### Render
   1. Create an account on [Render](https://render.com/)
   2. Create a new Web Service
   3. Connect your GitHub repository
   4. Add environment variables (DISCORD_TOKEN)
   5. Deploy

   ### Heroku
   1. Create an account on [Heroku](https://heroku.com/)
   2. Create a new app
   3. Connect your GitHub repository
   4. Add environment variables (DISCORD_TOKEN)
   5. Deploy

## Commands

- `!ping` - Check if the bot is responsive
- `!join` - Bot joins your current voice channel
- `!leave` - Bot leaves the voice channel
- `!play <song name or URL>` - Play a song
- `!pause` - Pause the current song
- `!resume` - Resume the paused song
- `!stop` - Stop playing and clear the queue

## Troubleshooting

1. **FFmpeg not found**
   - Ensure FFmpeg is installed correctly
   - Verify the FFmpeg path in `bot.py`
   - Check if FFmpeg is in your system PATH

2. **Bot not joining voice channel**
   - Ensure the bot has proper permissions
   - Check if you're in a voice channel
   - Verify the bot's voice permissions in Discord

3. **Music not playing**
   - Check your internet connection
   - Verify FFmpeg installation
   - Ensure the bot has proper permissions

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 