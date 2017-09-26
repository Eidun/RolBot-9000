from discord.ext import commands
from rules.jsonreader import Reader


class RulesCommands:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def new_rules(self, ctx, name: str, param1=None):
        """Nuevas reglas añadidas adaptadas de 5 anillos a Akuma.
        Secciones
            arquetipos
            entrenamientos
            flujo_de_creacion
            historial
            magia (proximamente)
            reglas_generales (proximamente)
            ventajas_desventajas
            experiencia
            habilidades (proximamente)"""
        result = Reader().get_json(name, param1)
        if result.__len__() == 3:
            out = result[0] + "\n para continuar, añade la reacción 👍"
            msg = await self.wait_emoji(ctx.message.author, str(out), '👍')
            out = result[1] + "\n para continuar, añade la reacción 👍"
            await self.bot.delete_message(msg)
            msg = await self.wait_emoji(ctx.message.author, str(out), '👍')
            await self.bot.delete_message(msg)
            out = result[2] + "\n para finalizar, añade la reacción 👍"
            msg = await self.wait_emoji(ctx.message.author, str(out), '👍')
            await self.bot.delete_message(msg)
        else:
            await self.bot.send_message(ctx.message.author, result)

    async def wait_emoji(self, channel, message: str, emoji):
        msg = await self.bot.send_message(channel, message)
        ret = await self.bot.wait_for_reaction([emoji], message=msg)
        return msg


def setup(bot):
    bot.add_cog(RulesCommands(bot))
