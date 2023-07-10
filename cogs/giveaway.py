import random
from discord.ext import commands

class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.giveaways = {}

    @commands.command()
    async def giveaway(self, ctx, action, *args):
        if action == 'start':
            await self.start_giveaway(ctx, *args)
        elif action == 'end':
            await self.end_giveaway(ctx)
        elif action == 'reroll':
            await self.reroll_giveaway(ctx)
        elif action == 'list':
            await self.list_giveaway(ctx)
        elif action == 'help':
            await self.giveaway_help(ctx)

    async def start_giveaway(self, ctx, reward, duration, winners, *requirements):
        # Start a giveaway with the provided information
        giveaway_id = str(random.randint(1000, 9999))
        self.giveaways[giveaway_id] = {
            'reward': reward,
            'duration': duration,
            'winners': winners,
            'requirements': requirements,
            'participants': []
        }
        await ctx.send(f'Giveaway started! ID: {giveaway_id}')

    async def end_giveaway(self, ctx):
        # End the current giveaway
        # Select winners and announce them
        giveaway_id = self.get_active_giveaway_id()
        if giveaway_id:
            giveaway = self.giveaways[giveaway_id]
            winners = random.sample(giveaway['participants'], giveaway['winners'])
            await ctx.send(f'Giveaway ended! Winners: {", ".join(winners)}')
            del self.giveaways[giveaway_id]
        else:
            await ctx.send('No active giveaway.')

    async def reroll_giveaway(self, ctx):
        # Reroll the winners for the current giveaway
        giveaway_id = self.get_active_giveaway_id()
        if giveaway_id:
            giveaway = self.giveaways[giveaway_id]
            winners = random.sample(giveaway['participants'], giveaway['winners'])
            await ctx.send(f'Giveaway rerolled! New winners: {", ".join(winners)}')
        else:
            await ctx.send('No active giveaway.')

    async def list_giveaway(self, ctx):
        # List all users enrolled in the giveaway
        giveaway_id = self.get_active_giveaway_id()
        if giveaway_id:
            giveaway = self.giveaways[giveaway_id]
            participants = giveaway['participants']
            await ctx.send('Participants:\n' + '\n'.join(participants))
        else:
            await ctx.send('No active giveaway.')

    async def giveaway_help(self, ctx):
        # Provide information about the giveaway command
        help_message = """
        Giveaway Command:
        /giveaway start <reward> <duration> <winners> [requirements] - Start a giveaway
        /giveaway end - End the current giveaway and announce winners
        /giveaway reroll - Reroll winners for the current giveaway
        /giveaway list - List all users enrolled in the giveaway
        /giveaway help - Show this help message
        """
        await ctx.send(help_message)

    def get_active_giveaway_id(self):
        # Get the ID of the active giveaway
        for giveaway_id, giveaway in self.giveaways.items():
            if giveaway['participants']:
                return giveaway_id
        return None

def setup(bot):
    bot.add_cog(Giveaway(bot))
