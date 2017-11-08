import discord
from discord.ext import commands
from economy.agent import Agent


class EconomyCommands:

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def eco(self, ctx):
        """Todo lo relacionado con la economía"""
        if ctx.invoked_subcommand is None:
            await self.bot.say('Debes poner un subcomando!')

    @eco.command()
    async def status(self, name: str):
        agent = Agent(name)
        await self.bot.say('Nombre: {} Balance: {}'.format(agent.name, agent.amount))


def setup(bot):
    bot.add_cog(EconomyCommands(bot))

