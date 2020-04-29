# -*- coding: UTF-8 -*- 
import discord
import random
from discord.ext import commands
import json
import os


def locked(ctx):#codigo para bloquear comandos
    return ctx.author.id == 122727645132750848


prefixo = "*"
build = 'HE12020/04/29'
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


@client.command(name='habilitar', help='habilita um comando')
async def habilitar(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} foi habilitado!')


@client.command(name='desabilitar', help='desabilita um comando')
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
