# 007-Bot
Discord Bot to Spy 

This bot uses ADB with an emulated copy of Evony:TKR running on Bluestacks to spy on an enemy server during SVS week.

Commands:

!spy - Takes a screenshot of the world chat on the enemy server and posts it in discord on demand.

!startspying - Takes a screenshot of the world chat on the enemy server and posts it in discord.  Every 5 seconds it takes a new screenshot and compares it with the old one.  If they are different it deletes the current discord message with the old screenshot and sends a new message with the new screenshot.  This keeps the bot from spamming the channel with many messages.
