import random
from discord.ext import commands

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx):
        # Roll a 6-sided dice
        roll = random.randint(1, 6)
        await ctx.send(f':game_die: You rolled a {roll}!')

def setup(bot):
    bot.add_cog(Dice(bot))
