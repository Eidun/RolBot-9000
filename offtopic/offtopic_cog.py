import discord
import asyncio
from discord.ext import commands
from offtopic.memes import Memes


class OffTopic_Commands:

    def __init__(self, bot):
        self.bot = bot
        self.Meme = Memes()


    @commands.command()
    async def empanado(self, loser: discord.Member):
        """Menciona a un usuario que esté empanado."""
        for i in range(3):
            await self.bot.send_message(loser, 'Empanado, responde')
            await asyncio.sleep(3)

    @commands.command(pass_context=True)
    async def meme(self, ctx, *name: str):
        """El humor es lo más sano del mundo, riámonos con los
        memes personalizados de los jugadores.
        Para reacciones aceptadas, use !meme list"""
        if(len(name)  != 0):
            if(name[0]=="add"):
                if(len(name) >= 3):
                    message = self.Meme.add_meme(name[1], name[2])
                else:
                    message = "le faltan parametros al comando"
            elif(name[0]=="list"):
                message = self.Meme.get_list();
            elif(name[0]=="delete" ):
                if(len(name) >= 2):
                    message = self.Meme.delete_meme(name[1])
                else:
                    message = "le faltan parametros al comando"
            else:
                    message = self.Meme.get_meme(name[0])
        else:
            message = "le faltan parametros al comando"
        await self.bot.send_message(ctx.message.channel, message)


def setup(bot):
    bot.add_cog(OffTopic_Commands(bot))
