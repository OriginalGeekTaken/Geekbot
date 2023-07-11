import disnake
from disnake.ext import commands
import openai
import requests
from bs4 import BeautifulSoup
from config import openai_api_key

openai.api_key = openai_api_key

class cat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conversations = []
        self.cached_doc_content = None
        self.doc_url = 'https://docs.google.com/document/d/e/2PACX-1vSc_mYJ5NBpCj1PLhQcU_AKUR15c4vZdFLDGiCxek2e-vxdPqS2SK7XlVnXMIw9Ujv_1lnH-Nm41U7F/pub'

    @commands.command()
    async def cat(self, ctx):
        user_id = str(ctx.author.id)
        message = ctx.message.content[5:]  # Remove '/cat ' from the message

        self.conversations.append(message)

        try:
            response = self.get_snarky_response(user_id, message)
            self.conversations.append(response)
            await ctx.send(response)
        except Exception as e:
            await ctx.send("Sorry, an error occurred while processing the request.")

    def get_google_doc_content(self):
        if self.cached_doc_content is not None:
            return self.cached_doc_content

        try:
            response = requests.get(self.doc_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            doc_content = [p.get_text() for p in paragraphs]

            self.cached_doc_content = doc_content
            return doc_content
        except (requests.RequestException, ValueError) as e:
            raise Exception("Error occurred while fetching Google Document content.") from e

    def get_snarky_response(self, user_id, message):
        # Access the content of the Google Doc
        doc_content = self.get_google_doc_content()

        # Perform OpenAI conversation and reference the Google Doc content
        conversation = self.conversations + doc_content
        prompt = 'Geekbot:' + ''.join([f'\nUser: {msg}' for msg in conversation])

        try:
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=prompt,
                max_tokens=50,
                temperature=0.7,
                n=1,
                stop=None,
            )
            return response.choices[0].text.strip().split('\n')[-1].replace('Geekbot:', '')
        except openai.OpenAIError as e:
            raise Exception("Error occurred while communicating with OpenAI API.") from e

def setup(bot):
    bot.add_cog(cat(bot))
