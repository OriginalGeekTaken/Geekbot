import json
from discord.ext import commands

class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        # Warn the specified user
        warnings = self.load_warnings()
        if str(member.id) not in warnings:
            warnings[str(member.id)] = []
        warnings[str(member.id)].append(reason)
        self.save_warnings(warnings)
        await ctx.send(f'{member.name} has been warned.')

    def load_warnings(self):
        # Load warnings from warnings.json
        try:
            with open('warnings.json', 'r') as file:
                warnings = json.load(file)
        except FileNotFoundError:
            warnings = {}
        return warnings

    def save_warnings(self, warnings):
        # Save warnings to warnings.json
        with open('warnings.json', 'w') as file:
            json.dump(warnings, file)

def setup(bot):
    bot.add_cog(Warn(bot))
