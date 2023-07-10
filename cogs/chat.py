import openai
from discord.ext import commands

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.openai_api_key = 'YOUR_OPENAI_API_KEY'

    @commands.command()
    async def chat(self, ctx, *, message):
        # Chat with ChatGPT 3.5 and receive responses
        response = self.chat_with_openai(message)
        await ctx.send(response)

    def chat_with_openai(self, message):
        # Chat with OpenAI ChatGPT 3.5
        openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ],
            max_tokens=50
        )

def setup(bot):
    bot.add_cog(Chat(bot))
