import discord
import asyncio
from discord.ext import commands
from memes import Memes
from jsonreader import Reader
from roliador import Roliador
from dossier import  Dossier
from info_card import InfoCard
from values import MODE

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
async def oceanic(*identificadores: str):
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
            color=0xFFFFFF
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
        embed.add_field(name='Descripción',value=info[7])
        embed.set_image(url=info[8])

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

@bot.command(pass_context=True)
async def new_rules(ctx, name: str, param1=None):
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
        msg = await wait_emoji(ctx.message.author, str(out), '👍')
        out = result[1] + "\n para continuar, añade la reacción 👍"
        await bot.delete_message(msg)
        msg = await wait_emoji(ctx.message.author, str(out), '👍')
        await bot.delete_message(msg)
        out = result[2] + "\n para finalizar, añade la reacción 👍"
        msg = await wait_emoji(ctx.message.author, str(out), '👍')
        await bot.delete_message(msg)
    else:
        await bot.send_message(ctx.message.author, result)


async def wait_emoji(channel, message: str, emoji):
    msg = await bot.send_message(channel, message)
    ret = await bot.wait_for_reaction([emoji], message=msg)
    return msg


@bot.command(pass_context=True)
async def meme(ctx, name: str):
    """El humor es lo más sano del mundo, riámonos con los
    memes personalizados de los jugadores.
    Reacciones aceptadas
    malvado
    mafioso
    meto_maldad
        """

    with open(Memes().get_meme(name), 'rb') as f:
        await bot.send_file(ctx.message.channel, f)


if MODE == 0:
    # RolBot-9000
    bot.run('MzU2NzExNTA3NjYyNDcxMTY4.DJnDKw.4ehhHUJtoWT7rslw-gzRinIrZVE')
else:
    # Testbot-9000
    bot.run('MTg3MTU3Nzk1MjA2ODU2NzA0.DJm8Sg.FyRDFpoSarSq2LC6wTpU3VfFTIQ')
