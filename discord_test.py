import discord
from discord.ext import commands
import asyncio
import sys

TOKEN = "MTA4ODE2ODA1MjcyMzU2MDUwOA.GWOWLk.2P8jPw6xb0U_vJc89iP23M7CKzpYzdWa8XJx8o"

#intents = discord.Intents.default()
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def get_user_id(server, username):
    async for member in server.fetch_members():
        if member.name.lower() == username.lower():
            return member.id
        elif (member.name + "#" + member.discriminator).lower() == username.lower():
            return member.id
    return None

async def check_username(server, username):
    async for member in server.fetch_members():
        if member.name.lower() == username.lower():
            return True
    return False

async def check_username_full(server, username_discriminator):
    async for member in server.fetch_members():
        if (member.name + "#" + member.discriminator).lower() == username_discriminator.lower():
            return True
    return False

async def main(server_id, username):
    await bot.wait_until_ready()
    server = bot.get_guild(server_id)
    if server is None:
        print("Server not found. Make sure the bot is a member of the server.")
        return

    exists = await check_username(server, username)
    id_exists = await get_user_id(server, username)

    exists_full = await check_username_full(server, username)
    id_exists_full = await get_user_id(server, username)

    if exists:
        print(f"Username '{username}' exists on the server.")
        print(f"User ID: {id_exists}")
        
    elif exists_full:
        print(f"Username '{username}' exists on the server.")
        print(f"User ID: {id_exists_full}")
    else:
        print(f"Username '{username}' does not exist on the server.")
    await bot.close()

@bot.event
async def on_ready():
    server_id = int(sys.argv[1])
    username = sys.argv[2]
    await main(server_id, username)

'''
@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower() == "!server_id":
        guild_id = message.guild.id
        await message.channel.send(f"The server ID is: {guild_id}")

    await bot.process_commands(message)
#message_history = last5(1068147950280245369)

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower() == "!last5":
        messages = await message.channel.history(limit=6).flatten()
        response = "Last 5 messages:\n"
        for msg in reversed(messages[1:]):
            response += f"{msg.author}: {msg.content}\n"
        await message.channel.send(response)

    await bot.process_commands(message)
'''
    
bot.run(TOKEN)

#server_id = 980797272830902322
#bot_token = MTA4ODE2ODA1MjcyMzU2MDUwOA.GWOWLk.2P8jPw6xb0U_vJc89iP23M7CKzpYzdWa8XJx8o
#all privileged intents enabled