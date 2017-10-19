import discord
from discord.ext import commands
import random
import re
bot = commands.Bot(command_prefix='', description='JeffBot')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)


@bot.event
async def on_message(message):
    if re.search("pphedd", message.content, flags=0):
        tmp = await bot.send_message(message.channel, 'pp')

    if re.search("jeff", message.content, flags=0):
        tmp = await bot.send_message(message.channel, 'HAHAHAHAHA FUNNY MEME YO SO JOKE LOL HAHA MA NAEM JEFF')
    if re.search("<@!244933944175362048>", message.content, flags=0):
        tmp = await bot.send_message(message.channel, 'AY DONT PING MY CREATOR ASSBUTT!1!')


    await bot.process_commands(message)


@bot.command()
async def roll():
    a = random.randrange(1-20)
    await bot.say(a)



bot.run('<Redacted>')
