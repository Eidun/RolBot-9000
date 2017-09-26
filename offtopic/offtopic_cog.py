import discord
import asyncio
from discord.ext import commands
from offtopic.memes import Memes


class OffTopic_Commands:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def empanado(self, loser: discord.Member):
        """Menciona a un usuario que esté empanado."""
        for i in range(3):
            await self.bot.send_message(loser, 'Empanado, responde')
            await asyncio.sleep(3)

    @commands.command(pass_context=True)
    async def meme(self, ctx, name: str):
        """El humor es lo más sano del mundo, riámonos con los
        memes personalizados de los jugadores.
        Reacciones aceptadas
        malvado
        mafioso
        meto_maldad
            """

        with open(Memes().get_meme(name), 'rb') as f:
            await self.bot.send_file(ctx.message.channel, f)


def setup(bot):
    bot.add_cog(OffTopic_Commands(bot))
