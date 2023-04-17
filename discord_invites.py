import discord
from discord.ext import commands
import asyncio
import sys

TOKEN = "YOUR_BOT_TOKEN"

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def check_username(server, username, discriminator):
    async for member in server.fetch_members():
        if member.name.lower() == username.lower() and member.discriminator == discriminator:
            return True
    return False

async def send_invite_link(user_id, server):
    user = await bot.fetch_user(user_id)
    if user is None:
        print("User not found.")
        return

    # Create an invite link for the server's general channel
    general_channel = discord.utils.get(server.text_channels, name="general")
    if general_channel is None:
        print("No general channel found.")
        return

    invite = await general_channel.create_invite(max_uses=1, unique=True)
    await user.send(f"Hello! You have been invited to join the server: {invite.url}")

async def main(server_id, username, discriminator, user_id):
    await bot.wait_until_ready()
    server = bot.get_guild(server_id)
    if server is None:
        print("Server not found. Make sure the bot is a member of the server.")
        return

    exists = await check_username(server, username, discriminator)
    if exists:
        print(f"Username '{username}#{discriminator}' exists on the server.")
    else:
        print(f"Username '{username}#{discriminator}' does not exist on the server.")
        await send_invite_link(user_id, server)
    await bot.close()

@bot.event
async def on_ready():
    server_id = int(sys.argv[1])
    username = sys.argv[2]
    discriminator = sys.argv[3]
    user_id = int(sys.argv[4])
    await main(server_id, username, discriminator, user_id)

bot.run(TOKEN)
