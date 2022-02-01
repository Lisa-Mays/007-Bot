from asyncio.windows_events import NULL
import discord
from discord import client
from discord import file
from discord.client import Client
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import os
import time
import sys
import hashlib

BUF_SIZE = 65536
bot = commands.Bot(command_prefix='!')
doispy = False

# Function to create hash from image file
def gethash(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

# Function get a screenshot of the screen to compare and turn into hash
def getss()->str:
    print("getss function: taking a screenshot...")
    os.system('cmd /c "adb shell screencap -p /sdcard/chat2.png"')
    # Pull image to PC
    os.system('cmd /c "adb pull /sdcard/chat2.png /Users/Hopes/Desktop/ETKO/chat2.png"')
    time.sleep(1)
    print("We got the screenshot and hashed it")
    hash2 = gethash("/Users/Hopes/Desktop/ETKO/chat2.png")
    print(hash2)
    return (hash2)

# When bot connects set the bots activity status message
@bot.event
async def on_ready():
    print('Connected!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Server 736"))

@bot.command(pass_context=True)
async def startspying(ctx):
        print("Do i spy value is: ")
        global doispy
        doispy = True
        print(doispy)
        print("Setting hash 1 to null...")
        hash1 = NULL
        print("Uploading initial image and pausing 15 seconds")
        # Upload first image message in the cycle
        getss()
        channel = bot.get_channel(Insert Channel ID)
        dismsg = await ctx.send(file=discord.File('/Users/Hopes/Desktop/ETKO/chat2.png'))
        time.sleep(15)
        while doispy == True:
            time.sleep(5)
            print("running getss function to get hash 2 and new screenshot...")
            getss()
            hash2 = getss()
            print("Comparing hash 1 to hash 2 and waiting 5 seconds")
            time.sleep(5)
            # Compare Images and update Spy Channel when image is different run entire thing every 5 seconds
            if hash1 != hash2:
                # delete existing message
                print("attempting to delete existing message...")
                await dismsg.delete()
                # upload chat 2 discord picture
                print("Uploading new picture message to discord...")
                channel = bot.get_channel(Insert Channel ID)
                dismsg = await ctx.send(file=discord.File('/Users/Hopes/Desktop/ETKO/chat2.png'))
                time.sleep(5)
                print("Uploaded first image to chat")
                # Remove chat 1 on computer
                os.remove("chat1.png")
                print("Deleting chat1 file from computer..")
                # Rename chat2 to chat 1 on computer
                os.rename("chat2.png", "chat1.png")    
                print("Renamed file...")
                hash1 = hash2   
                print("Swapped hashes...")
        else:
            print("Images were the same, deleting images and watiing to check again...")
            # Delete second image from phone
            os.system('cmd /c "adb shell rm /sdcard/chat2.png"')
            # Delete second image from computer
            os.remove('chat2.png')

@bot.command(pass_context=True)
async def stopspying(ctx):
    global doispy
    doispy = False

# Spy command to send spy screenshot to discord on demand
@bot.command(pass_context=True)
async def spy(ctx):
    # delete old screenshot on computer
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

bot.run('Insert Bot Token')

