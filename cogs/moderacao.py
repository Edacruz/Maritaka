import discord
from discord.ext import commands


class moderação(commands.Cog):
    def __init__(self, client):
        self.client = client


    #limpar mensagens
    @commands.command(name='limpar', help='apaga uma dada quantidade de mensagens.', aliases=['clear','deletar','del'])
    @commands.has_permissions(manage_messages=True)
    async def limpar(self, ctx, amount=1):
        if amount >= 100: 
            return await ctx.send('Limite excedido, eu posso limpar apenas 99 mensagens por vez.')
        elif amount < 1:
            await ctx.send('Digite um número válido!')
        else:    
            await ctx.channel.purge(limit = amount + 1)

            if amount > 1: 
                await ctx.send(f'{amount} mensagens deletadas por <@{ctx.message.author.id}>')   
            else:
                await ctx.send(f'{amount} mensagem deletada por <@{ctx.message.author.id}>')


    #kick
    @commands.has_permissions(kick_members=True)
    @commands.command(name='kick', help='Expulsa um usuário do servidor.', aliases=['expulsar'])
    async def kick(self, ctx, member : discord.Member, *, motivo=None):
        await member.kick(reason=motivo)
        await ctx.send(f'{member} foi expulso.\nMotivo: {motivo}')
    #ban
    @commands.has_permissions(ban_members=True)
    @commands.command(name='ban', help='Bane um usuário do servidor.', aliases=['banir'])
    async def ban(self, ctx, member : discord.Member, *, motivo=None):
        try:
            await member.ban(reason=motivo) 
        except discord.Forbidden:
            await ctx.send(f'Você precisa ter permissão para `banir usuários` para executar este comando. ')
        else:
            await ctx.send(f'{member} foi banido.\nMotivo: {motivo}')

    #unban
    @commands.has_permissions(ban_members=True)
    @commands.command(name='unban', help='Desbane um usuário do servidor.')
    async def unban(self, ctx, *, member):
        usuarios_banidos = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in usuarios_banidos:
            user = ban_entry.user
            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.name}#{user.discriminator} foi desbanido!')
                return


def setup(client):
	client.add_cog(moderação(client))
