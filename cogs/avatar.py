from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        # Get the larger version of the specified user's avatar
        avatar_url = member.avatar_url_as(size=1024)
        await ctx.send(avatar_url)

def setup(bot):
    bot.add_cog(Avatar(bot))
