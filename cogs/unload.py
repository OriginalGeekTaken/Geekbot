from discord.ext import commands

class Unload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unload(self, ctx, cog):
        # Unload a cog (module) from the bot
        try:
            self.bot.unload_extension(f'cogs.{cog}')
            await ctx.send(f'{cog} has been unloaded.')
        except commands.ExtensionNotFound:
            await ctx.send(f'{cog} does not exist.')
        except commands.ExtensionNotLoaded:
            await ctx.send(f'{cog} is not loaded.')

def setup(bot):
    bot.add_cog(Unload(bot))
