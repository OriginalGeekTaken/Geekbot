from discord.ext import commands

class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unban(self, ctx, member_id: int):
        # Unban the user from the server
        banned_users = await ctx.guild.bans()
        for entry in banned_users:
            if entry.user.id == member_id:
                await ctx.guild.unban(entry.user)
                await ctx.send(f'{entry.user.name} has been unbanned.')
                return

def setup(bot):
    bot.add_cog(Unban(bot))
