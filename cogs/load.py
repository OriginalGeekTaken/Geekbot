from discord.ext import commands

class Load(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def load(self, ctx, cog):
        # Load a cog (module) into the bot
        try:
            self.bot.load_extension(f'cogs.{cog}')
            await ctx.send(f'{cog} has been loaded.')
        except commands.ExtensionNotFound:
            await ctx.send(f'{cog} does not exist.')
        except commands.ExtensionAlreadyLoaded:
            await ctx.send(f'{cog} is already loaded.')

def setup(bot):
    bot.add_cog(Load(bot))
