# -*- coding: UTF-8 -*- 
# Maritaka bot versão 0.1
import discord
import asyncio
import random

client = discord.Client()
token = 'NjYwMzUzMjczNjU5OTE2Mjk5.XgbtCw.eYuTEZUxw4KJjJBW_AN_izx1WNY'

#imprimindo status
@client.event
async def on_ready():
        print('Bot online!')
        print(client.user.name,'está online!')
        print(client.user)

#eventos de mensagem
@client.event
async def on_message(message):
    if message.content.startswith('?oi'):
        channel = message.channel
        await client.send_message(message.channel,'Saudações, {} '.format(message.author))
    if message.content.startswith('?help'):
        channel = message.channel
        await client.send_message(message.channel,'Bot criando por: Marbas Lag da Silva Stark, she was born in 2019/12/28, at: 14:09.')
    if message.content.startswith('hey, maritaka, quem é a melhor waifu?'):
        channel = message.channel
        await client.send_message(message.channel,'Essa deve ser eu kiki :blush:')

    if 'Feliz aniversario' in message.content.lower() and message.author != client.user:
        await client.send_message(message.channel,'Feliz aniversário! 🎈🎉')
    if message.content.startswith('?marbas'):
        channel = message.channel
        await client.send_message(message.channel,'O Marbas é foda!')

#rodando o client
client.run(token)

