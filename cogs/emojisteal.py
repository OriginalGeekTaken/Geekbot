from discord.ext import commands

class Emojisteal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def emojisteal(self, ctx, emoji: discord.Emoji):
        # Retrieve the image file for the specified emoji
        await ctx.send(emoji.url)

def setup(bot):
    bot.add_cog(Emojisteal(bot))
