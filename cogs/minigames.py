import discord
from discord.ext import commands
import random
import json
from uteis import fish


class joguinhos(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name='dado', help='Lança um dado.', aliases=['dice'])
	async def dado(self, ctx, lados: int = 6, qt_dados: int = 1):
	    dado = [
	        str(random.choice(range(1, lados + 1)))
	        for _ in range(qt_dados)
	    ]
	    await ctx.send(', '.join(dado))


	#faz o bot contar até o numero estipulado.
	@commands.cooldown(1, 16, commands.BucketType.user)
	@commands.command(name='flood', help='Faz um flood maneiro. ', aliases=['spam'])
	async def flood(self, ctx, maximo: int,*, mensagem='default'):   
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
	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command(name='jackpot', help='Sorteia 3 números.', aliases=['jp'])
	async def jackpot(self, ctx):
	    sorteio = (random.randint(0,9),random.randint(0,9),random.randint(0,9))#tupla que recebe os números sorteados
	    #testanto se todos os números são iguais
	    if sorteio[0] == sorteio[1] and sorteio[2] == sorteio[0] and sorteio[1] != 6:
	        await ctx.send(f'{sorteio}\nJackpot! 🎉\nVocê venceu!, <@{ctx.author.id}>')
	    elif sorteio[0] == 6 and sorteio[1] == sorteio[2] and sorteio[0] == sorteio[1]:
	        await ctx.send(f'{sorteio}\nJackpot! 🎉\nSatanic win! 🤘️, <@{ctx.author.id}>')
	    else:
	        await ctx.send(f'{sorteio}\n<@{ctx.author.id}>, Você perdeu 😭 ') 


	@commands.command(name='moeda', help='Lança uma moeda para tirar cara ou coroa.', aliases=['coin'])
	async def moeda(self, ctx):
	        moeda = random.randint(0,1)
	        if moeda == 1:
	            await ctx.send('😉 | **Cara!**')
	        else:
	            await ctx.send('👑 | **Coroa!**')


	@commands.cooldown(1, 4, commands.BucketType.user)
	@commands.command(name='joguinho', help='Joguinho de advinhar o número.', aliases=['joguin'])
	async def joguin(self, ctx, sua_escolha: int):
	    numero = [0,1,2,3,4,5,6,7,8,9]
	    sekai = random.choice(numero)
	    if sua_escolha == sekai:
	        await ctx.send(f'Você escolheu: **{sua_escolha}**\n<@{ctx.author.id}>, você ganhou :partying_face:')
	    elif sua_escolha not in numero:
	        await ctx.send('Digite um número entre 0 e 9 😐️')
	    else:
	        await ctx.send(f'<@{ctx.author.id}>, você perdeu 😭 \nVocê escolheu: **{sua_escolha}**\nResposta certa: **{sekai}**')


	@commands.cooldown(1, 6, commands.BucketType.user)
	@commands.command(name='pescar', help='Pesca virtual xD', aliases=['fish'])
	async def pescar(self, ctx):
		user = ctx.author.id
		fish.existe('dados/inventario.json', user) #checando se o usuario está cadastrado na base de dados
		lago = (random.randint(0,250),random.randint(0,250),random.randint(0,250),random.randint(0,250))
		peixe = lago[0]+lago[1]+lago[2]+lago[3]

		
		if peixe < 750:
			await ctx.send('🎣| Você pegou um peixe **comum** 🐟')
			fish.pegarpeixe("dados/inventario.json","peixe-c", user)
			fish.ler("dados/inventario.json")
	
		elif peixe > 750 and peixe < 950:
			await ctx.send('🎣| Você pegou um peixe **incomum** 🐡')
			fish.pegarpeixe("dados/inventario.json","peixe-u", user)

		elif peixe > 950 and peixe < 995:
			await ctx.send('🎣| Você pegou um peixe **raro** 🐠')
			fish.pegarpeixe("dados/inventario.json","peixe-r", user)

		else:
			await ctx.send('🎣| Você pegou um peixe **lendário** 🦈')
			fish.pegarpeixe("dados/inventario.json","peixe-l", user)



	@commands.command(name='inventario', help='mostra seu inventário', aliases=['i'])
	async def inventario(self, ctx):
		usuario = ctx.author.id
		with open('dados/inventario.json','r') as f:
			data = json.load(f)
		for casa in data:
			if casa["id"] == usuario:
				await ctx.send(f'<@{casa["id"]}> Seu inventário contem:  \n**Comum** 🐟: {casa["peixe-c"]} \n**Incomum** 🐡: {casa["peixe-u"]} \n**Raro** 🐠: {casa["peixe-r"]} \n**Lendário** 🦈: {casa["peixe-l"]}')


		


def setup(client):
	client.add_cog(joguinhos(client))
	