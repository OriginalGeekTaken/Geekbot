import random
from discord.ext import commands

class EightBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def eightball(self, ctx):
        # Provide random responses similar to the 8 ball toy
        responses = [
            'Yes',
            'No',
            'Maybe',
            'Ask again later',
            'Outlook not so good',
            'Definitely',
            'It is certain',
            'Cannot predict now'
        ]
        response = random.choice(responses)
        await ctx.send(response)

def setup(bot):
    bot.add_cog(EightBall(bot))
