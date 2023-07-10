from discord.ext import commands

class Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        # Get information about the current server
        server = ctx.guild
        owner = server.owner
        creation_date = server.created_at.strftime('%Y-%m-%d %H:%M:%S')
        member_count = server.member_count
        info_message = f'Server Name: {server.name}\nOwner: {owner}\nCreation Date: {creation_date}\nMember Count: {member_count}'
        await ctx.send(info_message)

def setup(bot):
    bot.add_cog(Serverinfo(bot))
