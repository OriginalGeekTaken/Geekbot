from discord.ext import commands

class Banlist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def banlist(self, ctx):
        # Get the list of banned users
        banned_users = await ctx.guild.bans()
        banlist = [f'{entry.user.name} - {entry.user.id}' for entry in banned_users]
        await ctx.send('\n'.join(banlist))

def setup(bot):
    bot.add_cog(Banlist(bot))
