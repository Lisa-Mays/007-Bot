import discord
from discord import client
from discord import file
from discord.client import Client
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt
import os
import time

bot = commands.Bot(command_prefix='!')


# Change status of discord bot when it connects to discord
@bot.event
async def on_ready():
    print('Connected!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Server 540"))

# Wait for spy command in discord then send a screenshot of server chat to discord channel
@bot.command(pass_context=True)
async def spy(ctx):
    # Delete old screenshot on computer
    os.remove("screen1.png")
    time.sleep(1)
    # Get a screenshot of the screen 
    os.system('cmd /c "adb shell screencap -p /sdcard/screen.png"')
    # Pull image to PC
    os.system('cmd /c "adb pull /sdcard/screen.png /Users/Hopes/Desktop/ETKO/screen1.png"')
    time.sleep(1)
    # Send image to discord
    channel = bot.get_channel(Insert Channel ID)
    await ctx.send(file=discord.File('screen1.png'))
    # Delete image from phone
    os.system('cmd /c "adb shell rm /sdcard/screen.png"')

bot.run('Insert Bot Token Here')
