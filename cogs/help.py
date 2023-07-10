from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        # Display help information
        help_message = """
        List of Commands:
        /kick - Kick a user
        /ban - Ban a user
        /banlist - Show the list of banned users
        /unban - Unban a user
        /warn - Warn a specified user
        /warnings - Show warnings of a specified user
        /avatar - Show a larger version of specified user's profile picture or avatar
        /embed - Create a rich and interactive embed message
        /help - Show this help message
        """
        await ctx.send(help_message)

def setup(bot):
    bot.add_cog(Help(bot))
