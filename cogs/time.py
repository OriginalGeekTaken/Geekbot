import datetime
import pytz
from discord.ext import commands

class Time(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def time(self, ctx, location):
        # Get the current time for the specified location
        try:
            timezone = pytz.timezone(location)
            current_time = datetime.datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
            await ctx.send(f'Current Time in {location}: {current_time}')
        except pytz.UnknownTimeZoneError:
            await ctx.send(f'Unknown Timezone: {location}')

def setup(bot):
    bot.add_cog(Time(bot))
