import discord
from discord.ext import commands
from dislash import SlashClient, ActionRow, Button

TOKEN = "MTA4ODE2ODA1MjcyMzU2MDUwOA.GWOWLk.2P8jPw6xb0U_vJc89iP23M7CKzpYzdWa8XJx8o"

intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)
slash = SlashClient(bot)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready!")

@slash.command(
    name="buttons",
    description="Show buttons"
)
async def buttons(ctx):
    button1 = Button(style=discord.ButtonStyle.primary, label="Button 1", custom_id="button1")
    button2 = Button(style=discord.ButtonStyle.primary, label="Button 2", custom_id="button2")

    await ctx.send("Here are some buttons:", components=[ActionRow(button1, button2)])

@slash.component_callback()



'''
async def button1(ctx):
   #call google calendar api on button click

   await ctx.send("You clicked Button 1!", hidden=True)

@slash.component_callback()
async def button2(ctx):
    await ctx.send("You clicked Button 2!", hidden=True)

bot.run(TOKEN)
'''