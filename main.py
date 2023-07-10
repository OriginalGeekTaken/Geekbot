import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Load Cogs
bot.load_extension('cogs.kick')
bot.load_extension('cogs.ban')
bot.load_extension('cogs.banlist')
bot.load_extension('cogs.unban')
bot.load_extension('cogs.warn')
bot.load_extension('cogs.warnings')
bot.load_extension('cogs.avatar')
bot.load_extension('cogs.embed')
bot.load_extension('cogs.help')
bot.load_extension('cogs.load')
bot.load_extension('cogs.unload')
bot.load_extension('cogs.ping')
bot.load_extension('cogs.say')
bot.load_extension('cogs.dice')
bot.load_extension('cogs.eightball')
bot.load_extension('cogs.aww')
bot.load_extension('cogs.emojisteal')
bot.load_extension('cogs.giveaway')
bot.load_extension('cogs.purge')
bot.load_extension('cogs.serverinfo')
bot.load_extension('cogs.time')
bot.load_extension('cogs.weather')
bot.load_extension('cogs.chat')

bot.run('<INSERT.DISCORD.BOT.TOKEN.HERE>')
