import json
from discord.ext import commands

class Warnings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def warnings(self, ctx, member: discord.Member):
        # Get the warnings of the specified user
        warnings = self.load_warnings()
        if str(member.id) in warnings:
            user_warnings = warnings[str(member.id)]
            await ctx.send(f'Warnings for {member.name}:\n' + '\n'.join(user_warnings))
        else:
            await ctx.send(f'{member.name} has no warnings.')

    def load_warnings(self):
        # Load warnings from warnings.json
        try:
            with open('warnings.json', 'r') as file:
                warnings = json.load(file)
        except FileNotFoundError:
            warnings = {}
        return warnings

def setup(bot):
    bot.add_cog(Warnings(bot))
