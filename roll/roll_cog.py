from discord.ext import commands
from roll.roliador import Roliador
import values


class RollCog:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def roll(self, ctx, number: int, modo="Normal"):
        """Tira un número de D10"""
        roliador = Roliador()
        if modo == "cobarde":
            roliador.repeat = -1
        if modo == "PROFETA":
            respond = roliador.profeta()
        else:
            results = roliador.roll(number)
            respond = roliador.pretty_print_discord(ctx.message.author, results)

        await self.bot.say(respond)

    @commands.command(pass_context=True)
    async def ndn(self, ctx, xdy: str):
        """Tira formato NdN"""
        number, faces = xdy.split('d', 1)
        roliador = Roliador(int(faces), -1)
        results = roliador.roll(int(number))
        respond = roliador.pretty_print_discord(ctx.message.author, results)

        await self.bot.say(respond)

    @commands.command(hidden=True)
    async def set_initial(self, number: int):
        values.initial_number = number

    @commands.command(pass_context=True)
    async def custom(self, ctx, *dices: int):
        """Tira lo que pongas"""
        roliador = Roliador(10, -1)
        results = roliador.custom_roll(dices)
        respond = roliador.custom_pretty_print_discord(ctx.message.author, results)

        await self.bot.say(respond)


def setup(bot):
    bot.add_cog(RollCog(bot))
