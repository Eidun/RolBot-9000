import discord
from memes import Memes
from discord.ext import commands
from dossier import Dossier
from roliador import Roliador
from jsonreader import Reader

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
async def meme(ctx, name:str):
    """El humor es lo más sano del mundo, riámonos con los
    memes personalizados de los jugadores.
    Reacciones aceptadas
    malvado
    mafioso
    meto_maldad
        """

    print(name)
    with open(Memes().get_meme(name), 'rb') as f:
        await bot.send_file(ctx.message.channel, f)

    @bot.command(pass_context=True)
    async def meme(ctx, name: str):
        """El humor es lo más sano del mundo, riámonos con los
        memes personalizados de los jugadores.
        Reacciones aceptadas
        malvado
        mafioso
        meto_maldad
            """

        print(name)
        with open(Memes().get_meme(name), 'rb') as f:
            await bot.send_file(ctx.message.channel, f)

@bot.command(pass_context=True)
async def new_rules(ctx, name: str, param1 = None):
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
    if(result.__len__() == 3):
        out = result[0] + "\n para continuar, añade la reacción 👍"
        msg = await wait_emoji(ctx.message.author, str(out), '👍')
        out = result[1] + "\n para continuar, añade la reacción 👍"
        await bot.delete_message(msg)
        msg = await wait_emoji(ctx.message.author, str(out),'👍')
        await bot.delete_message(msg)
        out = result[2]+ "\n para finalizar, añade la reacción 👍"
        msg = await wait_emoji(ctx.message.author, str(out),'👍')
        await bot.delete_message(msg)
    else:
        await bot.send_message(ctx.message.author, result)

async def wait_emoji(channel, message:str, emoji):
    msg = await bot.send_message(channel, message)
    ret = await bot.wait_for_reaction([emoji], message=msg)
    return msg
# RolBot-9000
#bot.run('MzU2NzExNTA3NjYyNDcxMTY4.DJnDKw.4ehhHUJtoWT7rslw-gzRinIrZVE')
# Subnorbot
bot.run('MTg3MTY1MTAxODk4NDY1Mjgw.DJrz5g.bkoW0IGwnHj4CF0KF_tu9G-s_l8')
