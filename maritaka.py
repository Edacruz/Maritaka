# -*- coding: UTF-8 -*- 
# Maritaka bot versão 0.3
import discord
import asyncio
import random

versao = '0.4'
build = 'HE 12020/03/07'
client = discord.Client()
token = 'dicord_token'

#imprimindo status
@client.event
async def on_ready():
        print('Bot online!')
        print(client.user.name,'está online!')
        print(client.user)
        print(client.user.id)

#=-=-==-=-= eventos de mensagem =-=-==-=-=
@client.event
async def on_message(message):
    if message.content.startswith('?oi') and message.author != client.user:
        channel = message.channel
        await client.send_message(message.channel,'Saudações, <@{}>'.format(message.author.id))
    if message.content.startswith('?irineu') and message.author != client.user:
        channel = message.channel
        nome = [message.author]
        await client.send_message(message.channel,'{}, não sabe nem eu\n{}'.format(message.author,nome))


    if message.content.startswith('?sobre') and message.author != client.user:
        channel = message.channel
        await client.send_message(message.channel,'Bot criando por: Marbas Lag da Silva Stark, she was born in HE12019/12/28, at 14:09.\nDigite **?comandos** para ver todos os comados.\n*versão do bot: {}\nversão do Python: 3.5.1*\nBuild date: **{}** '.format(versao,build))


    if message.content.startswith('hey, maritaka quem é a melhor waifu?') and message.author != client.user:
        channel = message.channel
        await client.send_message(message.channel,'Essa deve ser eu kiki :blush:')


    if 'melhor waifu' in message.content.lower():
        await client.send_message(message.channel,'Essa deve ser eu')


    if message.content.startswith('?marbas') and message.author != client.user:
        channel = message.channel
        await client.send_message(message.channel,'Lorde Marbas é o meu criador, ele gosta de vacas \'-\'')


    if message.content.startswith('?sub') and message.author != client.user:
        channel = message.channel
        await client.send_message(message.channel,'O Sub não é um escravo, só ganha mal')


    if message.content.startswith('?tainaka') and message.author != client.user:
        channel = message.channel
        await client.send_message(message.channel,'A Tainaka gosta de alface :thinking:')


    if message.content.startswith('?chauri') and message.author != client.user:
        channel = message.channel
        await client.send_message(message.channel,'É a webesposa do lorde Marbas, e é também uma deusa.')


    if message.content.startswith('?maritaka') and message.author != client.user:
        msg = message.content
        if len(msg) <= 9:
            await client.send_message(message.channel,'Digite algo!\nSintax: `?maritaka <mensagem>`')
        else:
            channel = message.channel
            await client.send_message(message.channel,msg[9:])
    
    #se o bot for marcado
    if '660353273659916299' in message.content and message.author != client.user:
        frases = ['Oi','Sup!','Eae','Chamou, sir?','Ao seu dispor','Sim, esta sou eu','Ay ay, sir!','Tô a fazer chá','Estou a apreciar a beleza do lorde marbas, não enche!','dormindo :sleeping:']
        await client.send_message(message.channel,random.choice(frases))

#=-=-==-=-= fim dos eventos de mensagem =-=-==-=-=

#flood
    if message.content.startswith('?flood'):
        msg = message.content
        if len(msg) < 8:
            await client.send_message(message.channel,'Digite um valor válido!\nSintax: `?flood <limite>`')
        elif message.author.id == "user_id":#nega a permissão para um usuário
            maximo = 0
            await client.send_message(message.channel,'Você não tem permissão pra usar este comando!')
        elif int(msg[7:]) > 50:
            await client.send_message(message.channel,'Limite excedido, digite um valor menor que 50')
            maximo = 0    
        else:
            maximo = int(msg[7:])  
        spam = 0
        while spam < maximo:
            spam += 1
            msg = message.content
            channel = message.channel
            if maximo > 0:
                await client.send_message(message.channel, spam)
                
#fim da tag de flood


#=-=-=-=-= código dos joguinhos =-=-=-=-=


#=-=-=-=-= codigo do jackpot =-=-=-=-=
    if message.content.startswith('?jackpot') and message.author != client.user:
        
        #Sorteando numeros:
        sorteio = (random.randint(0,9),random.randint(0,9),random.randint(0,9))

        channel = message.channel

        #testanto se todos os números são iguais
        if sorteio[0] == sorteio[1] and sorteio[2] == sorteio[0]:
            await client.send_message(message.channel,'{}\nJackpot! 🎉'.format(sorteio))
        #se eu perder não serei chamado de otário kkkk
        elif sorteio[0] != sorteio[1] and message.author.id == "122727645132750848" or sorteio[2] != sorteio[0] and message.author.id == "122727645132750848":
            await client.send_message(message.channel,'{}\nTu perdeste, lindo :sob:'.format(sorteio))
        else:
            await client.send_message(message.channel,'{}\nPerdeu, otário! <@{}>'.format(sorteio,message.author.id)) 
#=-=-=-=-= fim do codigo do jackpot =-=-=-=-=

#=-=-=-=-= joguinho de adivinhar número (a ser implementado) =-=-=-=-=
    if message.content.startswith('?joguin') and message.author != client.user:
        msg = message.content
        if len(msg) <= 7:
            await client.send_message(message.channel,('Digite algo!\nSintax: `?joguin <numero entre 0 e 9>`'))
        else:
            #fatiando a string para pegar apenas o número 
            sua_escolha = msg[8:]
            await client.send_message(message.channel,'Você escolheu: **{}**'.format(sua_escolha))
            numero = ['0','1','2','3','4','5','6','7','8','9']
            sekai = random.choice(numero)
            if sua_escolha == sekai:
                await client.send_message(message.channel,'Você ganhou :partying_face:')
            elif sua_escolha not in ['0','1','2','3','4','5','6','7','8','9']:
                await client.send_message(message.channel,'Digite um número entre 0 e 9 :expressionless:')
            else:
                await client.send_message(message.channel,'\nResposta certa: **{}**\nVocê perdeu :sob: '.format(sekai))
#
#
#=-=-=-=-= fim joguinho de adivinhar número =-=-=-=-=

#-=-=-=-= Jogo de cara ou coroa -=-=-=-=-=-=-=-=
    if message.content.startswith('?moeda'):
        msg = message.content
        moeda = random.randint(0,1)
        if moeda == 1:
            await client.send_message(message.channel,"Cara :wink:")
        else:
            await client.send_message(message.channel,"Coroa :crown:") 
#=-=-=-=-=-= fim dos joguinhos -=-=-=-=-=-=-=-=-=-=
                
#mostra todos os comandos: 
    if message.content.startswith('?comandos'):
        msg = message.content
        channel = message.channel
        await client.send_message(message.channel,'```?marbas\n?tainaka\n?sub\n?maritaka\n?oi\n?chauri\n?flood\n?jackpot\n?joguin\n?moeda```\n*Digite `?info <comando>` para ter detalhes.*')

#comandos de descrição:
#    if message.content.startswith('?info joguin'):
#        channel = message.channel
#        await client.send_message(message.channel,'Joguinho de adivinhar um número.\nsintax: `joguin <numero entre 0 e 9>`')


#versão
    if message.content.startswith('?v'):
        msg = message.content
        channel = message.channel
        await client.send_message(message.channel,'*Maritaka versão: {}*'.format(versao))
   

#rodando o client
client.run(token)

