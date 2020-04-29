import discord
from discord.ext import commands


class interações(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name='slap', help='da um tapa em alguém')
	async def slap(self, ctx, target):
		slap = discord.Embed(
	        title = None,
	        description = f'<@{ctx.author.id}> has slaped {target}, and now he\'s crying.',
	        colour = discord.Colour.blue()
	    )
		slap.set_image(url='https://img1.ak.crunchyroll.com/i/spire4/d84e88fa3152f01a113a184296ab4baa1369808004_full.png')
		slap.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
		await ctx.send(embed=slap)


def setup(client):
	client.add_cog(interações(client))