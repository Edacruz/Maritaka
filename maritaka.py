# -*- coding: UTF-8 -*- 
import discord
import asyncio
import random
from discord.ext import commands
import json
import os


def locked(ctx):#codigo para bloquear comandos
    return ctx.author.id == 122727645132750848


prefixo = "*"
build = 'HE12020/04/19'
client = commands.Bot(command_prefix=prefixo)
chave = open('key.txt','r')
token = chave.read()#aqui vai o tolken do bot
chave.close

#imprimindo status do bot
@client.event
async def on_ready():
        print('=-'*10,'.:ONLINE:.','-='*10)
        print(client.user.name,'está online!')
        print('Cliente user: ',client.user)
        print('Cliente user id: ',client.user.id)
        print('=-'*10,'xxFIMxxx','-='*10)
        #setando o status online do bot. online = online; não perturbe = dnd; ausente = idle;
        await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Fazendo chá.'))


@client.command()
async def habilitar(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} foi habilitado!')


@client.command()
async def desabilitar(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} foi desabilitado!')    


#=-=-==-=-=*** Main Commands ***=-=-==-=-=
@client.command(name='oi', help='Faz a Maritaka dar-te oi.')
async def oi(ctx):
    saudacoes = ['Saudações','Olá','Salve','Eae','Coé','Fala!','Sup']
    await ctx.send(f'{random.choice(saudacoes)}, <@{ctx.author.id}>')

@client.command(name='ping', help='Retorna o ping do bot.')
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')


@client.command(name='dado', help='Lança um dado.')
async def dado(ctx, lados: int = 6, qt_dados: int = 1):
    dado = [
        str(random.choice(range(1, lados + 1)))
        for _ in range(qt_dados)
    ]
    await ctx.send(', '.join(dado))

@client.command(name='irineu', help='Você não sabe nem eu.')
async def irineu(ctx):
    await ctx.send(f'<@{ctx.author.id}>, não sabe nem eu.')

@client.command(name='sobre', help='Sobre o bot.')
async def sobre(ctx):
    await ctx.send(f'Bot criando por: **Marbas L.S. Stark**, she was born in **HE12019/12/28**, at 14:09.\nDigite **{prefixo}help** para ver todos os comados.\nversão do Python: 3.6.9*\n*Build date:* **{build}** ')

#deuses
@client.command(name='gi', help='Mostra a descrição de todos os deuses.\nChauri, Gabriel, Marbas, Sub, Tainaka.')
async def gi(ctx, deus="all"):
    if deus.lower() == 'marbas':
        await ctx.send('Lorde Marbas é o meu criador, ele gosta de vacas \'-\'')
    elif deus.lower() == 'chauri':
        await ctx.send('Deusa da beleza e da fofura, é também esposa do lorde Marbas.')
    elif deus.lower() == 'tainaka' or deus == 'tainara':
        await ctx.send('Tainaka é a deusa dos alfaces 🤔')
    elif deus.lower() == 'sub':
        await ctx.send('Sub é o deus do trabalho voluntário.')
    elif deus.lower() == 'gabriel':
        await ctx.send('É o deus ou deusa das traps, é também o rei dos disfarces 👌')
    else:
        await ctx.send(f'Sintaxe incorrecta! digite: `{prefixo}gi <deus>`')

#=-=-=-=-=-=-=-=xxx Fim da descrição dos deuses xxx=-=-=-=-=-=-=-=

#comando que repete a mensagem enviada
@client.command(name='maritaka', help='Repete a sua mensagem.', aliases=['say','diga','talk'])
async def say(ctx, *, mensagem):
    msg = ctx.message.content
    await ctx.channel.purge(limit = 1)
    await ctx.send(mensagem)


#faz o bot contar até o numero estipulado.
@client.command(name='flood', help='Faz um flood maneiro. ', aliases=['spam'])
async def flood(ctx, maximo: int,*, mensagem='default'):   
    if maximo > 100:
        await ctx.send('Limite excedido, digite um valor menor que 100.')
        maximo = 0 
    else:
        if mensagem == 'default':     
            for spam in range(0,maximo):
                await ctx.send(spam+1)
        else:
           for spam in range(0,maximo):
                await ctx.send(mensagem) 

#joguinho de jackpot, que gera 3 números aleatórios
@client.command(name='jackpot', help='Sorteia 3 números.', aliases=['jp'])
async def jackpot(ctx):
    sorteio = (random.randint(0,9),random.randint(0,9),random.randint(0,9))#tupla que recebe os números sorteados
    #testanto se todos os números são iguais
    if sorteio[0] == sorteio[1] and sorteio[2] == sorteio[0] and sorteio[1] != 6:
        await ctx.send(f'{sorteio}\nJackpot! 🎉\nVocê venceu!, <@{ctx.author.id}>')
    elif sorteio[0] == 6 and sorteio[1] == sorteio[2] and sorteio[0] == sorteio[1]:
        await ctx.send(f'{sorteio}\nJackpot! 🎉\nSatanic win! 🤘️, <@{ctx.author.id}>')
    else:
        await ctx.send(f'{sorteio}\n<@{ctx.author.id}>, Você perdeu 😭 ') 

@client.command(name='moeda', help='Lança uma moeda para tirar cara ou coroa.', aliases=['coin'])
async def moeda(ctx):
        moeda = random.randint(0,1)
        if moeda == 1:
            await ctx.send('😉 | **Cara!**')
        else:
            await ctx.send('👑 | **Coroa!**')

@client.command(name='joguinho', help='Joguinho de advinhar o número.', aliases=['joguin'])
async def joguin(ctx, sua_escolha: int):
    numero = [0,1,2,3,4,5,6,7,8,9]
    sekai = random.choice(numero)
    if sua_escolha == sekai:
        await ctx.send(f'Você escolheu: **{sua_escolha}**\n<@{ctx.author.id}>, você ganhou :partying_face:')
    elif sua_escolha not in numero:
        await ctx.send('Digite um número entre 0 e 9 😐️')
    else:
        await ctx.send(f'<@{ctx.author.id}>, você perdeu 😭 \nVocê escolheu: **{sua_escolha}**\nResposta certa: **{sekai}**')

@client.command(name='convite', help='Link para convidar o bot.', aliases=['convidar','invite'])
async def convite(ctx):
    await ctx.send('https://discordapp.com/oauth2/authorize?client_id=660353273659916299&permissions=537159744&scope=bot')




#=-=-==-=-=*** Eventos de mensagem ***=-=-==-=-=
@client.event
async def on_message(message):
    if message.author == client.user:
        return None
    canal = message.channel
    msg = message.content
    marcar = message.author.id

    #envia uma mensagem aleatória se o bot for marcado
    if '660353273659916299' in msg and message.author != client.user:
        await canal.send(f'Meu prefixo neste servidor é {prefixo}, <@{marcar}>')

    await client.process_commands(message)#sem esta linha os "comandos" não funcionam

#trantando exceções
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send('Ocorreu um error ao executar este comando.')
        print(f'{error}\n{commands.errors.CommandInvokeError}')

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Por favor informe os parâmetro necessários!') 

    elif isinstance(error, commands.errors.CommandNotFound):
        await ctx.send('Este comando não existe, verifique a ortografia.')
    elif isinstance(error, commands.errors.MissingPermissions):
        await ctx.send('Você não tem permissão para usar esse comando!')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#rodando o client
client.run(token)
