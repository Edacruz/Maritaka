# -*- coding: UTF-8 -*- 
import discord
import random
from discord.ext import commands
import json
import os


def is_owner(ctx):
    return ctx.author.id == 122727645132750848 or ctx.author.id == 662861778467684390


build = 'HE12020/05/08'
client = commands.Bot(command_prefix="m!", case_insensitive=True)
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
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Festa do chá.'))


@commands.check(is_owner)
@client.command(name='habilitar', help='habilita ums cog', aliases=['e'], hidden=True)
async def habilitar(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} foi habilitado!')


@commands.check(is_owner)
@client.command(name='desabilitar', help='desabilita uma cog', aliases=['d'], hidden=True)
async def desabilitar(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} foi desabilitado!')    


@commands.check(is_owner)
@client.command(name='reload', help='reinicia uma cog', aliases=['r'], hidden=True)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} foi reiniciado!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return None
    canal = message.channel
    msg = message.content
    marcar = message.author.id

    if '<@660353273659916299>' in msg and message.author != client.user:
        await canal.send(f'Precisando de ajuda? use **m!help** p/ ver meus comandos, <@{marcar}>')

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
        await ctx.send('Esse comando não existe.')
        pass

    elif isinstance(error, commands.errors.MissingPermissions):
        await ctx.send('Você não tem permissão para usar esse comando!')
        
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'<@{ctx.author.id}>, comando em cooldown, espere {round(error.retry_after, 2)} segundos.')
    
    elif isinstance(error, commands.errors.CheckFailure):
        await ctx.send('Error, are you sure that you are **The Master**?')
    else:
        raise error


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#rodando o client
client.run(token)
