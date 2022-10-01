from email import message
import discord
import os
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '!regras':
           await message.channel.send(f'Olá {message.author.name}, as regras do servidor são:{os.linesep} 1-Regra 1;{os.linesep}2-Regra 2;')
        if message.content == '!dm': 
            await message.author.send('Olá, tudo bem?')

Client = MyClient()
Client.run('mytoken')