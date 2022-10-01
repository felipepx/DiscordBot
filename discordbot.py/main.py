from email import message
import os
import discord
from discord.ext import commands

bot = commands.Bot('!')


@bot.event
async def on_ready():
    print(f'Logged on as! connect with {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'sensured' in message.content:

        await message.channel.send(f'Por Favor {message.author.name},  não ofenda os demais usuários!')

        await message.delete()

    await bot.process_commands(message)


# !oi
# send_hello


@bot.command(name='oi')
async def send_hello(ctx):
    name = ctx.author.name
    response = ' Olá, ' + name
    await ctx.send(response)


bot.run('token')
