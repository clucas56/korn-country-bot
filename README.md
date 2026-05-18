# Jennings County Korn Country 97.7 Discord Bot

A Discord bot that streams [Jennings County Korn Country 97.7 (WJCP)](https://www.korncountry.com) live into a Discord voice channel.

## Commands

| Command | Description |
|---|---|
| `/play` | Joins your current voice channel and starts the stream |
| `/stop` | Stops the stream and disconnects |
| `/nowplaying` | Shows what's currently streaming |

## Requirements

- Docker
- A Discord bot token ([Discord Developer Portal](https://discord.com/developers/applications))

## Setup

1. Clone the repo
   ```bash
   git clone https://github.com/clucas56/korn-country-bot.git
   cd korn-country-bot
   ```

2. Create a `.env` file
   ```
   BOT_TOKEN=your_bot_token_here
   ```

3. Run with Docker
   ```bash
   docker compose up -d
   ```

## Inviting the Bot

In the Discord Developer Portal, go to **OAuth2 → URL Generator** and select:
- Scopes: `bot`, `applications.commands`
- Permissions: `Connect`, `Speak`

Use the generated URL to invite the bot to your server.
