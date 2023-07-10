import random
import praw
from discord.ext import commands

class Aww(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                                  client_secret='YOUR_CLIENT_SECRET',
                                  user_agent='YOUR_USER_AGENT')

    @commands.command()
    async def aww(self, ctx):
        # Grab a random "aww" image from Reddit
        subreddit = self.reddit.subreddit('aww')
        posts = subreddit.hot(limit=50)
        images = [post.url for post in posts if post.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        image_url = random.choice(images)
        await ctx.send(image_url)

def setup(bot):
    bot.add_cog(Aww(bot))
