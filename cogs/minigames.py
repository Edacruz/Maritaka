import discord
from discord.ext import commands
import random
import json
import sqlite3


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


	@commands.cooldown(1, 4, commands.BucketType.user)
	@commands.group(name='pesca', help='Pesca virtual xD', aliases=['fish','f'])
	async def pescar(self, ctx):
		if ctx.invoked_subcommand is None:
			user = ctx.author.id
			peixe = random.randint(0,1000)
			pt = 0

			if 1 < peixe < 150:
				await ctx.send(f'🎣| Você pegou a **bota** 👢 do **! °•★ѕαкє★•°4052**')
				pt = 5

			elif 650 > peixe > 150:
				await ctx.send(f'🎣| Você pegou um peixe **comum** 🐟')
				pt = 1
				
			elif peixe > 650 and peixe < 950:
				await ctx.send(f'🎣| Você pegou um peixe **incomum** 🐡')
				pt = 2
				
			elif 1000 > peixe > 950:
				await ctx.send(f'🎣| <@{user}> Você pegou um peixe **raro** 🐠 cê é brabo mesmo hein')
				pt = 3
				
			else:
				await ctx.send(f'🎣| <@{user}> Você pegou um peixe **lendário** 🦈 {peixe}')
				pt = 4


			#conectando ao banco de dados:
			db = sqlite3.connect('main.sqlite')
			cursor = db.cursor()
			cursor.execute(f'SELECT * FROM inventario WHERE Id = {user}')
			result = cursor.fetchone()

			if result is None:#se o usuario ainda não estiver na base de dados
				print('NONE')
				sql = ('INSERT INTO inventario(Id, PeixeC,PeixeU,PeixeR,PeixeL,Worth) VALUES(?,?,?,?,?,?)')
				val = (user,0,0,0,0,0)
			elif result is not None:
				if pt == 1:
					sql = ("UPDATE inventario SET PeixeC = PeixeC+? WHERE Id = ?")
					val = (1,user)
				elif pt == 2:
					sql = ("UPDATE inventario SET PeixeU = PeixeU+?, Worth = Worth+? WHERE Id = ?")
					val = (1,3,user)
				elif pt == 3:
					sql = ("UPDATE inventario SET PeixeR = PeixeR+?, Worth = Worth+? WHERE Id = ?")
					val = (1,10,user)
				elif pt == 4:
					sql = ("UPDATE inventario SET PeixeL = PeixeL+?, Worth = Worth+? WHERE Id = ?")
					val = (1,50,user)
				elif pt == 5:
					sql = ("UPDATE inventario SET Garbage = Garbage+?, Worth = Worth+? WHERE Id = ?")
					val = (1,-2,user)
				
			cursor.execute(sql,val)
			db.commit()
			cursor.close()
			db.close()
			
	@pescar.command(name='inventario', help='mostra seu inventário', aliases=['i','inv'])
	async def inventario(self, ctx):
		user = ctx.author.id
		#conectando ao banco de dados:
		db = sqlite3.connect('main.sqlite')
		cursor = db.cursor()
		cursor.execute(f'SELECT * FROM inventario WHERE Id = {user}')
		result = cursor.fetchone()
		await ctx.send(f'Seu inventário de peixes:\n**Comum** 🐟: {result[1]}\n**Incomum** 🐡: {result[2]}\n**Raro** 🐠: {result[3]}\n**Lendário** 🦈: {result[4]}\n**Garbage** 💩: {result[6]}\n**Worth** ⭐: {result[5]} pontos.\n<@{ctx.author.id}> ')

	@pescar.command(name="rank", help="mostra os 10 maiores pescadores", aliases=["r"])
	async def rank(self,ctx):
		#conectando ao banco de dados:
		db = sqlite3.connect('main.sqlite')
		cursor = db.cursor()
		cursor.execute(f'SELECT Id, Worth FROM inventario ORDER BY Worth DESC LIMIT 10')
		result = cursor.fetchall()
		lst = len(result)
		rank = '**Top pescadores:**\n'
		for i in range(0,lst):
			if i == 0:
				colocacao = '🥇'
			elif i == 1:
				colocacao = '🥈'
			elif i == 2:
				colocacao = '🥉'
			else:
				colocacao = '⭐'

			rank += (f'{colocacao}| {i+1}º Lugar: {await self.client.fetch_user(result[i][0])} Worth: **{result[i][1]} Pontos**\n')
		await ctx.send(rank)

	
		

def setup(client):
	client.add_cog(joguinhos(client))
	