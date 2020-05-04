import discord
from discord.ext import commands


class matematica(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name='calc', help='calcula dois números. Apenas operações com dois números.', hidden=True)
	async def calc(self, ctx, n1, sinal, n2):
	    if sinal == '+':
	        s = float(n1) + float(n2)
	        await ctx.send('Soma: {:.1f}'.format(s))
	    elif sinal == '-':
	        s = float(n1) - float(n2)
	        await ctx.send('Subtração: {:.1f}'.format(s))
	    elif sinal == '*':
	        s = float(n1) * float(n2)
	        await ctx.send('Multiplicação: {:.1f}'.format(s))
	    elif sinal == '/':
	        s = float(n1) / float(n2)
	        await ctx.send('Divisão: {:.1f}'.format(s))
	    elif sinal == '%':
	        s = float(n1) % float(n2)
	        await ctx.send('Módulo: {:.1f}'.format(s))
	    elif sinal == '**':
	        s = float(n1) ** float(n2)
	        await ctx.send('Exponenciação: {:.1f}'.format(s))
        


def setup(client):
	client.add_cog(matematica(client))