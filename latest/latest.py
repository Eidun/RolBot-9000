import discord
from latest.ftp_adapter import get_last_file_url, HTTP_HOST
from discord.ext import commands
from bs4 import BeautifulSoup as bs
import requests
import asyncio
import aiohttp


class Latest:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def latest(self, ctx, subdir=None):
        """Sends a PM with the latest file's download URL.
        You can write the subdir desired"""
        # Get latest file
        file = get_last_file_url(subdir)

        # Check connection to FTP server
        if file is None:
            await self.bot.send_message(ctx.message.author, 'An error occurred with the files server')
            return
        # Check error file
        if file.date == 0:
            await self.bot.send_message(ctx.message.author, file.name)
            return

        # Building routes
        route = HTTP_HOST + file.path + file.name
        route = route.replace(' ', '%20')  # Removing whitespaces in the URL
        # PM Embed message
        embed = discord.Embed(title='Download link')
        embed.add_field(name='HTTP', value=route, inline=False)
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def soup(self, ctx):
        # Request
        request = requests.get('https://bato.to/group/_/a/atelier-du-noir-r6697')
        content = request.content
        # Preparing the soup
        soup = bs(content, 'html.parser')
        # Get table by class
        table = soup.find("table", {"class": "ipb_table chapters_list"})
        # Get all the table links
        links = table.findAll('a')
        # The first link is the desired
        url = links[1].get('href')
        # Creating the embed
        embed = discord.Embed()
        embed.add_field(name='URL', value='https://bato.to' + url)
        await self.bot.send_message(ctx.message.author, embed=embed)

    @commands.command(pass_context=True)
    async def aio_soup(self, ctx):
        loop = asyncio.get_event_loop()
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        new_loop.run_until_complete(get_site_content())
        asyncio.set_event_loop(loop)

async def get_site_content():
    async with aiohttp.ClientSession() as client:
        async with client.get('https://bato.to/group/_/a/atelier-du-noir-r6697') as resp:
            text = await resp.text()


def setup(bot):
    bot.add_cog(Latest(bot))
