# -*- coding: UTF-8 -*- 
# Maritaka bot versão 0.3.1
import discord
import asyncio
import random

versao = '0.3.1'
build = 'HE 12020/03/03'
client = discord.Client()
token = 'Discord Tolken'

#imprimindo status
@client.event
async def on_ready():
        print('Bot online!')
        print(client.user.name,'Está online!')
        print(client.user)
        print(client.user.id)

#=-=-==-=-= eventos de mensagem =-=-==-=-=
@client.event
async def on_message(message):
    if message.content.startswith('?oi') and message.author != client.user:
        channel = message.channel
        await client.send_message(message.channel,'Saudações, {}'.format(message.author))


    if message.content.startswith('?sobre') and message.author != client.user:
        channel = message.channel
        await client.send_message(message.channel,'Bot criando por: Marbas Lag da Silva Stark, she was born in HE12019/12/28, at 14:09.\nDigite **?comandos** para ver todos os comados.\n*versão do bot: {}\nversão do Python: 3.5.1*\nBuild date: **{}** '.format(versao,build))


    if message.content.startswith('hey, maritaka quem é a melhor waifu?') and message.author != client.user:
        channel = message.channel
        await client.send_message(message.channel,'Essa deve ser eu kiki :blush:')


    if 'Feliz aniversario' in message.content.lower() and message.author != client.user:
        await client.send_message(message.channel,'Feliz aniversário! 🎈🎉')


    if 'melhor waifu' in message.content.lower():
        await client.send_message(message.channel,'Essa deve ser eu')


    if message.content.startswith('?marbas') and message.author != client.user:
        channel = message.channel
        await client.send_message(message.channel,'O Marbas é o meu criador.')


    if message.content.startswith('?sub') and message.author != client.user:
        channel = message.channel
        await client.send_message(message.channel,'O Sub não é um escravo, só ganha mal')


    if message.content.startswith('?tainaka') and message.author != client.user:
        channel = message.channel
        await client.send_message(message.channel,'A Tainaka gosta de alface :thinking:')


    if message.content.startswith('?chauri') and message.author != client.user:
        channel = message.channel
        await client.send_message(message.channel,'É a webesposa do lorde Marbas, e também uma deusa entre os humanos.')


    if message.content.startswith('?maritaka') and message.author != client.user:
        msg = message.content
        channel = message.channel
        await client.send_message(message.channel,msg[9:])
    
    #se o bot for marcado
    if '660353273659916299' in message.content and message.author != client.user:
        frases = ['Oi','Sup!','Eae','Chamou, sir?','Ao seu dispor','Sim, esta sou eu','Ay ay, sir!','Tô a fazer chá','Estou a apreciar a beleza do lorde marbas, não enche!']
        await client.send_message(message.channel,random.choice(frases))

#=-=-==-=-= fim dos eventos de mensagem =-=-==-=-=

#flood
    if message.content.startswith('?flood'):
        spam = 0
        while True:
            spam += 1
            msg = message.content
            channel = message.channel
            await client.send_message(message.channel, spam)
            if 'pare' in message.content.lower():
                break  
                await client.send_message(message.channel, spam)
#fim da tag de flood

#=-=-=-=-= código dos joguinhos =-=-=-=-=


#=-=-=-=-= codigo do jackpot =-=-=-=-=
    if message.content.startswith('?jackpot') and message.author != client.user:
        
        #Sorteando numeros:
        sorteio = (random.randint(0,9),random.randint(0,9),random.randint(0,9))

        channel = message.channel
        await client.send_message(message.channel,sorteio)

        #testanto se todos os números são iguais
        if sorteio[0] == sorteio[1] and sorteio[2] == sorteio[0]:
            await client.send_message(message.channel,'Jackpot! 🎉')
        else:
            await client.send_message(message.channel,'Perdeu, otário!') 
#=-=-=-=-= fim do codigo do jackpot =-=-=-=-=

#=-=-=-=-= joguinho de adivinhar número (a ser implementado) =-=-=-=-=
#    if message.content.startswith('?joguin') and message.author != client.user:
#        await client.send_message(message.channel,'Digite um número ')
#        sua_escolha = message.content
#        numero = [0,1,2,3,4,5,6,7,8,9]
#        sekai = random.choice(numero)
#        if sua_escolha == sekai:
#            await client.send_message(message.channel,'você ganhou! ')
#        else:
#            await client.send_message(message.channel,'você não é tão bom assim é um #fracassado!',sekai)
#
#
#=-=-=-=-= fim joguinho de adivinhar número =-=-=-=-=
                
#mostra todos os comandos: 
    if message.content.startswith('?comandos'):
        msg = message.content
        channel = message.channel
        await client.send_message(message.channel,'```?marbas\n?tainaka\n?sub\n?maritaka\n?oi\n?chauri\n?flood\n?jackpot```\n*Digite `?help <comando>` para ter detalhes.*')

#versão
    if message.content.startswith('?v'):
        msg = message.content
        channel = message.channel
        await client.send_message(message.channel,'*Maritaka verão: {}*'.format(versao))
   

#rodando o client
client.run(token)

