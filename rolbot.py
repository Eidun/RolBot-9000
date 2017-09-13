import discord
import asyncio
from discord.ext import commands
import random
from roliador import Roliador
from dossier import  Dossier
from info_card import InfoCard

description = '''Soy RolBot9000, un ente interdimensional capaz de viajar entre los diferentes universos y mundos.

Tengo la capacidad analítica de predecir resultados heróicos y fatales si se me solicita. Bip...Bop...'''
bot = commands.Bot(command_prefix='!', description=description)




@bot.event
async def on_ready():
    print('RolBot9000 iniciándose...')
    print(bot.user.name)
    print(bot.user.id)
    print('Sistemas 100%')
    print('------')
    await bot.change_presence(game=discord.Game(name='rol con vosotros'))


@bot.command(pass_context=True)
async  def roll(ctx, number: int, modo="Normal"):
    """Tira un número de D10"""
    roliador = Roliador()
    if modo == "cobarde":
        roliador.repeat = -1
    if(modo == "PROFETA"):
       respond = roliador.profeta(number)
    else:
        results = roliador.roll(number)
        respond = roliador.pretty_print_discord(ctx.message.author, results)

    await bot.say(respond)


@bot.command(pass_context=True)
async  def ndn(ctx, xdy: str):
    """Tira formato NdN"""
    number, faces = xdy.split('d', 1)
    roliador = Roliador(int(faces), -1)
    results = roliador.roll(int(number))
    respond = roliador.pretty_print_discord(ctx.message.author, results)

    await bot.say(respond)


@bot.command(pass_context=True)
async  def custom(ctx, *dices: int):
    """Tira lo que pongas"""
    roliador = Roliador(10, -1)
    results = roliador.custom_roll(dices)
    respond = roliador.custom_pretty_print_discord(ctx.message.author, results)

    await bot.say(respond)


@bot.command()
async def empanado(loser: discord.Member):
    """Menciona a un usuario que esté empanado."""
    for i in range(3):
        await bot.send_message(loser, 'Empanado, responde')
        await asyncio.sleep(3)


@bot.command()
async def oceanic(name):
    """Información sobre el personaje requerido"""

    info = InfoCard(name).get_card()
    print(info)
    if info[1] == 'not found':
        embed = discord.Embed(
            title="Oceanic | Servicios",
            description="Lamentamos comunicarle que no tenemos información al respecto.",
            color=0xFFFFFF
        )
        embed.add_field(name="¿Quiere proporcionárnosla?", value="https://infobot9000.herokuapp.com")
    else:
        embed = discord.Embed(
            title=info[1],
            description=info[2],
            color=0x4C0099,
        )
        embed.add_field(name="Nombre", value=info[4], inline=True)
        embed.add_field(name="Alias", value=info[5], inline=True)
        embed.add_field(name="Posición", value=info[6], inline=True)
        embed.add_field(name='Descripción',
                        value=info[7])
        embed.set_thumbnail(url=info[8])

    await bot.say(embed=embed)


@bot.command()
async def nueva_info(organizacion='Desconocida', detalles='Desconocidos', color=0x4C0099, nombre='Desconocido',
                     alias='Desconocido', posicion='Desconocida', descripcion='Sin datos',
                     url_imagen='https://i.imgur.com/yPSG41I.png'):

    embed = discord.Embed(
        title=organizacion,
        description=detalles,
        color=color,
    )
    embed.add_field(name="Nombre", value=nombre, inline=True)
    embed.add_field(name="Alias", value=alias, inline=True)
    embed.add_field(name="Posición", value=posicion, inline=True)
    embed.add_field(name='Descripción', value=descripcion)
    embed.set_thumbnail(url=url_imagen)

    await bot.say(embed=embed)


@bot.command()
async def dossier(name:str):
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

    await bot.say(Dossier().get_dossier(name))

# RolBot-9000
bot.run('MzU2NzExNTA3NjYyNDcxMTY4.DJnDKw.4ehhHUJtoWT7rslw-gzRinIrZVE')
# Testbot-9000
# bot.run('MTg3MTU3Nzk1MjA2ODU2NzA0.DJm8Sg.FyRDFpoSarSq2LC6wTpU3VfFTIQ')
