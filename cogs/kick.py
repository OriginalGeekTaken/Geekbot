from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        # Kick the user from the server
        await member.kick(reason=reason)
        await ctx.send(f'{member.name} has been kicked.')

def setup(bot):
    bot.add_cog(Kick(bot))
