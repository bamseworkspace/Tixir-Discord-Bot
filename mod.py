import aiohttp
import warnings
import datetime
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class mod(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)
        
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason="This person has been banned"):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.name}#{member.discriminator}")
    
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason="This person has been kicked"):  
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.name}#{member.discriminator}")
    
    @commands.command()
    async def unban(self, ctx, *, member):
        bannedusers = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        
        for ban_entry in bannedusers:
            user = ban_entry.user
            
            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.name}#{user.discriminator}")
                return
            

    
        
def setup(client):
    client.add_cog(mod(client))
    