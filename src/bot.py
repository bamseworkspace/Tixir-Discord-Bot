
import os
import discord
from discord.ext import commands
import json

client = commands.Bot(command_prefix="!t")

client.remove_command("help")
@client.group(invoke_without_command=True)
async def help(ctx):
    embed1 = discord.Embed(
            title = "Help",
            colour = discord.Colour.blue()
        )
        
    # The Footer, Image, Auther, Fields
    
    embed1.set_footer(text = "Copyright (c) Bamsestudio 2022")
    embed1.set_author(name="Bamsestudio", icon_url="https://bamsestudio.dk/imgs/bs.png")
    embed1.add_field(name="load", value="Loads a cog", inline=False)
    embed1.add_field(name="unload", value="UnLoads a cog", inline=False)
    embed1.add_field(name="reload", value="ReLoads a cog", inline=False)
    embed1.add_field(name="clear", value="Clear some text with a amount", inline=False)
    embed1.add_field(name="ban", value="Bans a typed user", inline=False)
    embed1.add_field(name="kick", value="Kickes a typed user", inline=False)
    embed1.add_field(name="unban", value="Unbans a typed user", inline=False)
    embed1.add_field(name="info", value="Shows the info about the bot", inline=False)
    embed1.add_field(name="help", value="Shows This", inline=False)
    
    # Send the embed to the discord server
    await ctx.send(embed=embed1)

@client.command()
async def load(ctx, ext):
    client.load_extension(f"cogs.{ext}")
    
@client.command()
async def unload(ctx, ext):
    client.unload_extension(f"cogs.{ext}")
    
@client.command()
async def reload(ctx, ext):
    client.unload_extension(f"cogs.{ext}")
    client.load_extension(f"cogs.{ext}")
        
# Bot Things

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

with open("auth.json", "r") as file:
    tokendata = json.load(file)
    
token = tokendata["token"]
client.run(token)
