import discord
from discord.ext import commands

class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def embed(self, ctx):
        # Create and send an embed message
        embed = discord.Embed(title='Embed Title', description='Embed Description', color=discord.Color.blue())
        embed.set_author(name='Author Name', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Field 1', value='Value 1', inline=False)
        embed.add_field(name='Field 2', value='Value 2', inline=False)
        embed.set_footer(text='Embed Footer')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Embed(bot))
