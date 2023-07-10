from discord.ext import commands

class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def purge(self, ctx, amount: int):
        # Delete the specified amount of messages
        await ctx.channel.purge(limit=amount+1)

def setup(bot):
    bot.add_cog(Purge(bot))
