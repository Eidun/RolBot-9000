import sys
import traceback
import discord
from discord.ext import commands

import values

description = '''Soy RolBot9000, un ente interdimensional capaz de viajar entre los diferentes universos y mundos.
Tengo la capacidad analítica de predecir resultados heróicos y fatales si se me solicita. Bip...Bop...'''

modules = {'roll.roll_cog',
           'dossier.dossier_cog',
           'rules.rules_cog',
           'offtopic.offtopic_cog',
           'music.music_cog', }

bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('RolBot9000 iniciándose...')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name='rol con vosotros'))

    print('Cargando sistemas...')
    if __name__ == '__main__':
        for module in modules:
            try:
                bot.load_extension(module)
                print('\t' + module)
            except Exception as e:
                print(f'Error cargando la extension {module}', file=sys.stderr)
                traceback.print_exc()
    print('Sistemas 100%')
    print('------')


if values.MODE == 0:
    # RolBot-9000
    bot.run('MzU2NzExNTA3NjYyNDcxMTY4.DJnDKw.4ehhHUJtoWT7rslw-gzRinIrZVE')
else:
    # Testbot-9000
    bot.run('MTg3MTU3Nzk1MjA2ODU2NzA0.DJm8Sg.FyRDFpoSarSq2LC6wTpU3VfFTIQ')
