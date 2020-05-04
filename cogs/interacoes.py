import discord
from discord.ext import commands
from random import choice


class interações(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name='slap', help='da um tapa em alguém')
	async def slap(self, ctx, target):
		imgs = ['https://i.imgur.com/DVft5D6.gif','https://68.media.tumblr.com/382c5ecc93a0d1a9e4b7798d36f5cbeb/tumblr_oi01htdMfC1v57tj1o1_500.gif']
		if target.isnumeric():
			target = '<@'+target+'>'
		elif target.startswith != '<':
			target = '**' + target + '**'
		
		slap = discord.Embed(
	        title = None,
	        description = f'<@{ctx.author.id}> bateu em {target}',
	        colour = discord.Colour.blue()
	    )
		slap.set_image(url=choice(imgs))
		slap.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
		await ctx.send(embed=slap)


	@commands.command(name='pat', help='faz cafuné em alguém')
	async def pat(self, ctx, target):
		imgs = ['https://i.pinimg.com/originals/8b/42/6c/8b426c9bedc37054cd7e73925fa10da5.gif','https://media.tenor.com/images/1bf28037aa310fadf3711e703a65c3f1/tenor.gif','https://steamuserimages-a.akamaihd.net/ugc/916921610197525089/9CCD8DE73329F3F2840F77A96C03C082EE119421/','https://data.whicdn.com/images/297125682/original.gif','https://data.whicdn.com/images/297125550/original.gif','https://66.media.tumblr.com/2c546e729c79debbb9a04facff52b921/tumblr_n50nf50jj21qbvovho1_500.gifv','https://66.media.tumblr.com/584a3894e3483eed23d1afaf1f6f9347/tumblr_ok1oplyzSF1r0tp5lo1_1280.gifv']
		if target.isnumeric():
			target = '<@'+target+'>'
		elif target.startswith != '<':
			target = '**' + target + '**'
		
		pat = discord.Embed(
	        title = None,
	        description = f'<@{ctx.author.id}> fez cafuné em {target}',
	        colour = discord.Colour.blue()
	    )
		pat.set_image(url=choice(imgs))
		pat.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
		await ctx.send(embed=pat)


	@commands.command(name='kill', help='mata alguém')
	async def kill(self, ctx, target):
		imgs = ['https://i1.sndcdn.com/artworks-000250332043-sg3j6w-t500x500.jpg']
		if target.isnumeric():
			target = '<@'+target+'>'
		elif target.startswith != '<':
			target = '**' + target + '**'

		kill = discord.Embed(
	        title = None,
	        description = f'<@{ctx.author.id}> matou {target}',
	        colour = discord.Colour.blue()
	    )
		kill.set_image(url=choice(imgs))
		kill.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
		await ctx.send(embed=kill)


def setup(client):
	client.add_cog(interações(client))