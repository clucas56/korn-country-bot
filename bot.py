import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

STREAM_URL = "https://ice23.securenetsystems.net/WJCP"

intents = discord.Intents.default()
intents.voice_states = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.tree.command(name="play", description="Start streaming Jennings County Korn Country 97.7 in your voice channel")
async def play(interaction: discord.Interaction):
    member = await interaction.guild.fetch_member(interaction.user.id)
    if not member or not member.voice or not member.voice.channel:
        await interaction.response.send_message("You need to be in a voice channel first.", ephemeral=True)
        return

    channel = member.voice.channel

    # If already connected to a voice channel in this guild
    if interaction.guild.voice_client:
        if interaction.guild.voice_client.channel == channel:
            await interaction.response.send_message("Already streaming in your channel.", ephemeral=True)
            return
        await interaction.guild.voice_client.disconnect()

    await interaction.response.defer()

    vc = await channel.connect()
    vc.play(
        discord.FFmpegPCMAudio(STREAM_URL, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"),
    )

    await interaction.followup.send(f"Now streaming **Jennings County Korn Country 97.7** in **{channel.name}** 🎶")

@bot.tree.command(name="stop", description="Stop the stream and disconnect from voice")
async def stop(interaction: discord.Interaction):
    if not interaction.guild.voice_client:
        await interaction.response.send_message("Not currently in a voice channel.", ephemeral=True)
        return

    await interaction.guild.voice_client.disconnect()
    await interaction.response.send_message("Stopped the stream and disconnected.")

@bot.tree.command(name="nowplaying", description="Show what's currently streaming")
async def nowplaying(interaction: discord.Interaction):
    vc = interaction.guild.voice_client
    if vc and vc.is_playing():
        await interaction.response.send_message("Now playing: **Jennings County Korn Country 97.7** (WJCP 97.7 FM)")
    else:
        await interaction.response.send_message("Not currently streaming. Use `/play` to start.")

bot.run(os.getenv("BOT_TOKEN"))
