import discord
from discord.ext import commands

class normal(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def info(self, ctx):
        
        # init the embed
        embed1 = discord.Embed(
            title = "Information",
            description = "This bot is made by the Bamsestudio Team. And running on the Tixir Gaming Server...",
            colour = discord.Colour.blue()
        )
        
        # The Footer, Image, Auther, Fields
        
        embed1.set_footer(text = "Copyright (c) Bamsestudio 2022")
        embed1.set_image(url="https://bamsestudio.dk/imgs/bs.png")
        embed1.set_author(name="Bamsestudio", icon_url="https://bamsestudio.dk/imgs/bs.png")
        embed1.add_field(name="About The Bot", value="The bot is running on the disocrdAPI", inline=False)
        
        # Send the embed to the discord server
        await ctx.send(embed=embed1)
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game("Watching Tixir In The Eyes"))
        print("OnReady")
    
        
    
def setup(client):
    client.add_cog(normal(client))
    