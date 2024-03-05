import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def cek_tugas(ctx):
    url = 'https://slc.polinema.ac.id/spada/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Proses parsing tugas dari halaman Siakad
    # Contoh: tugas = soup.find('div', class_='tugas').text
    tugas = "Contoh tugas baru: Pertemuan 1: Perkenalan Developer - Bahasa Indonesia"
    if tugas:
        await ctx.send(f'Ada tugas baru: {tugas}')
    else:
        await ctx.send('Tidak ada tugas baru.')

bot.run('MTIxNDU3MDk5NTEwNTM5ODgwNA.GQxFK2.lHngFZdZeokRzoBAiRsbsvsLjOj0UiUt6NRa0A')
