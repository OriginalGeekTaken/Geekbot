import requests
from discord.ext import commands

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weather(self, ctx, location):
        # Get the current weather for the specified location
        api_key = 'YOUR_API_KEY'
        url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['current']['temp_c']
            condition = data['current']['condition']['text']
            await ctx.send(f'Weather in {location}: {condition}, {temperature}°C')
        else:
            await ctx.send(f'Failed to fetch weather for {location}')

def setup(bot):
    bot.add_cog(Weather(bot))
