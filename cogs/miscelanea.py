import discord
from discord.ext import commands
import random


class miscelânea(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command(name='oi', help='Faz a Maritaka dar-te oi.')
	async def oi(self, ctx):
	    saudacoes = ['Saudações','Olá','Salve','Eae','Coé','Fala!','Sup']
	    await ctx.send(f'{random.choice(saudacoes)}, <@{ctx.author.id}>')


	@commands.command(name='ping', help='Retorna o ping do bot.')
	async def ping(self, ctx):
	    await ctx.send(f'Pong! {round(self.client.latency*1000)}ms')


	@commands.command(name='irineu', help='Você não sabe nem eu.')
	async def irineu(self, ctx):
	    await ctx.send(f'<@{ctx.author.id}>, não sabe nem eu.')


	#deuses
	@commands.command(name='godinfo', help='Mostra a descrição de todos os deuses.\nChauri, Gabriel, Marbas, Sub, Tainaka.', aliases=['gi'])
	async def godinfo(self, ctx, deus="all"):
	    if deus.lower() == 'marbas':
	        await ctx.send('Lorde Marbas é o meu criador, ele gosta de vacas \'-\'')
	    elif deus.lower() == 'chauri':
	        await ctx.send('Deusa da beleza e da fofura, é também esposa do lorde Marbas.')
	    elif deus.lower() == 'tainaka' or deus == 'tainara':
	        await ctx.send('Tainaka é a deusa dos alfaces 🤔')
	    elif deus.lower() == 'sub':
	        await ctx.send('Sub é o deus do trabalho voluntário.')
	    elif deus.lower() == 'gabriel' or deus.lower() == 'tor':
	        await ctx.send('É o deus ou deusa das traps, é também o rei dos disfarces 👌')
	    elif deus.lower() == 'ado':
	    	await ctx.send('Ado é o deus dos teste vulgo cobaia')
	    else:
	        await ctx.send(f'Essa é a lista de deuses: Marbas; Tainaka; Gabriel; Sub; Ado.')


	#comando que repete a mensagem enviada
	@commands.command(name='maritaka', help='Repete a sua mensagem.', aliases=['say'])
	async def say(self, ctx, *, mensagem):
	    msg = ctx.message.content
	    await ctx.channel.purge(limit = 1)
	    await ctx.send(mensagem)

	@commands.command(name='sobre', help='Sobre o bot.', hidden=True)
	async def sobre(self, ctx):
	    await ctx.send(f'Bot criando por: **Marbas L.S. Stark**, she was born in **HE12019/12/28**, at 14:09.\nDigite **{prefixo}help** para ver todos os comados.\nversão do Python: 3.6.9*\n*Build date:* **{build}** ')


	@commands.command(name='convite', help='Link para convidar o bot.', aliases=['convidar','invite'])
	async def convite(self, ctx):
	    await ctx.send('https://discordapp.com/oauth2/authorize?client_id=660353273659916299&permissions=537159744&scope=bot')


def setup(client):
	client.add_cog(miscelânea(client))
