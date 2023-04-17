import discord
from discord.ext import commands

TOKEN = "MTA4ODE2ODA1MjcyMzU2MDUwOA.GWOWLk.2P8jPw6xb0U_vJc89iP23M7CKzpYzdWa8XJx8o"

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")
    await fetch_all_channels()

async def fetch_all_channels():
    for guild in bot.guilds:
        print(f"Server: {guild.name} (ID: {guild.id})")
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                print(f"  Channel: {channel.name} (ID: {channel.id})")
'''
#select a channel and send a message
async def send_message(channel_id, message):
    channel = bot.get_channel(channel_id)
    await channel.send(message)

message = "Test message generated using ChatGPT"
channel_id = 1088538218623934585

send_message(channel_id, message)
'''

'''Ask user for input and send a message to a channel
#ask user for input
async def ask_user():
    print("Enter a channel ID:")
    channel_id = int(input())
    print("Enter a message:")
    message = input()
    await send_message(channel_id, message)
'''

bot.run(TOKEN)
