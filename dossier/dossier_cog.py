import discord
from discord.ext import commands
from dossier.dossier import Dossier
from dossier.info_card import InfoCard


class DossierCommands:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def oceanic(self, *identificadores: str):
        """Información sobre el personaje requerido"""

        full_ident = list(identificadores)
        identificador = ''
        for ident in full_ident:
            identificador += ident + ' '
        identificador = identificador[:-1]

        info = list(InfoCard(identificador).get_card())
        if info[1] == 'not found':
            embed = discord.Embed(
                title="Oceanic | Servicios",
                description="Lamentamos comunicarle que no tenemos información al respecto.",
                color=0x0f5ea3
            )
            embed.add_field(name="¿Quiere proporcionárnosla?", value="https://infobot9000.herokuapp.com")
        else:
            for i in range(info.__len__()):
                if info[i] is None or info[i] == "":
                    info[i] = "Desconocido"

            embed = discord.Embed(
                title=info[1],
                description=info[2],
                color=0x4C0099,
            )
            embed.add_field(name="Nombre", value=info[4], inline=True)
            embed.add_field(name="Alias", value=info[5], inline=True)
            embed.add_field(name="Posición", value=info[6], inline=True)
            embed.add_field(name='Descripción', value=info[7])
            embed.set_image(url=info[8])

        await self.bot.say(embed=embed)

    @commands.command()
    async def dossier(self, name: str):
        """Muestra las páginas del dossier que indiques.
        Grupos disponibles:
            agencia
            d13
            oversight
            zehcs gebet
            deadcell
            ektors
            ordo
            oversight
            utopia
            otros """

        await self.bot.say(Dossier().get_dossier(name))


def setup(bot):
    bot.add_cog(DossierCommands(bot))
