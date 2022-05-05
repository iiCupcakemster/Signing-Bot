from webserver import keep_alive
import os
import traceback
from replit import db
import aiohttp
import sys
from io import BytesIO
import datetime
import humanfriendly
from dotenv import load_dotenv
import random
import difflib
from difflib import SequenceMatcher as sq
import asyncio
#pip install nextcord
import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import application_checks
from nextcord.ext import commands
from nextcord import abc,ChannelType
from nextcord import Member
from nextcord import Role
from nextcord.utils import get
from nextcord import ButtonStyle
from nextcord.ui import Button,View
import requests
import asyncio
BASE = "https://nextcord.com/api/v9/"
import cooldowns
from cooldowns import get_remaining_calls,cooldown,SlashBucket,CallableOnCooldown

#pip install function-cooldowns

# db['Guild'] = 901932361229410334
# db['Ownerrole'] = 954845327465271336
# db['Managerrole'] = db['Ownerrole']
# db['Modrole'] = db['Ownerrole']
# db['Adminrole'] = db['Ownerrole']


Intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="-", intents=Intents, case_insensitive = True) 
bot.remove_command('help')


# if db['BottomImage'] in db[]

errorimage = "https://media4.giphy.com/media/oWomIKXp66Lcruo9uT/giphy.gif?cid=6c09b9527ybrnh1zgixyh432w2t26u5ncnft554feb5fpw55&rid=giphy.gif&ct=s"
utilitiesimage = "https://thumbs.gfycat.com/HeartfeltRecklessAgama-max-1mb.gif"
notificationimage = "https://cdn.dribbble.com/users/2514055/screenshots/5538470/__.gif"
verdictimage = "https://media4.giphy.com/media/MZY3W2ARx79Ug9tgwY/giphy.gif"
modimage = "https://cdn.rcimg.net/Meta_comic/images/78998c9a/223cae48849c8e896365467232e22ac2.gif?width=300&quality=10&blur=20"
tradeimage = "https://www.cmegroup.com/trading/metals/images/commoditydirect-barchart.gif"
timeimage = "https://upload.wikimedia.org/wikipedia/commons/7/7a/Alarm_Clock_GIF_Animation_High_Res.gif"



if 'Color' in db.keys():
  pass
else:
  db['Color'] = 0x2F3136


HCname = "Head Coach" 
FOname = "Franchise Owner" 
GMname = "General Manager" 
Chiefsname = "Kansas City Chiefs"
Vikingsname = "Minnesota Vikings"
Cowboysname = "Dallas Cowboys"
Packersname = "Green Bay Packers"
ninersname = "San Francisco 49ers"
Buccaneersname = "Tampa Bay Buccaneers"
Eaglesname = "Philadelphia Eagles"
Steelersname = "Pittsburgh Steelers"
Seahawksname = "Seattle Seahawks"
Bearsname = "Chicago Bears"
Brownsname = "Cleveland Browns"
Dolphinsname = "Miami Dolphins"
Raidersname = "Las Vegas Raiders"
Giantsname = "New York Giants"
Broncosname = "Denver Broncos"
Jetsname = "New York Jets"
Billsname = "Buffalo Bills"
Washingtonname = "Washington Commanders"
Panthersname = "Carolina Panthers"
Ravensname = "Baltimore Ravens"
Saintsname = "New Orleans Saints"
Patriotsname = "New England Patriots"
Falconsname = "Atlanta Falcons"
Coltsname = "Indianapolis Colts"
Cardinalsname = "Arizona Cardinals"
Ramsname = "Los Angeles Rams"
Bengalsname = "Cincinnati Bengals"
Titansname = "Tennessee Titans"
Texansname = "Houston Texans"
Chargersname = "Los Angeles Chargers"
Jaguarsname = "Jacksonville Jaguars"
Lionsname = "Detroit Lions"

@bot.event
async def on_ready():
  bot.league = bot.get_guild(db['Guild'])
  bot.Chiefsrole = nextcord.utils.get(bot.league.roles, name=Chiefsname)
  bot.Vikingsrole = nextcord.utils.get(bot.league.roles, name=Vikingsname)
  bot.Cowboysrole = nextcord.utils.get(bot.league.roles, name=Cowboysname)
  bot.Dolphinsrole = nextcord.utils.get(bot.league.roles, name=Dolphinsname)
  bot.Packersrole = nextcord.utils.get(bot.league.roles, name=Packersname)
  bot.ninersrole = nextcord.utils.get(bot.league.roles, name=ninersname)
  bot.Buccaneersrole = nextcord.utils.get(bot.league.roles, name=Buccaneersname)
  bot.Eaglesrole = nextcord.utils.get(bot.league.roles, name=Eaglesname)
  bot.Steelersrole = nextcord.utils.get(bot.league.roles, name=Steelersname)
  bot.Seahawksrole = nextcord.utils.get(bot.league.roles, name=Seahawksname)
  bot.Bearsrole = nextcord.utils.get(bot.league.roles, name=Bearsname)
  bot.Brownsrole = nextcord.utils.get(bot.league.roles, name=Brownsname)
  bot.Dolphinsrole = nextcord.utils.get(bot.league.roles, name=Dolphinsname)
  bot.Raidersrole = nextcord.utils.get(bot.league.roles, name=Raidersname)
  bot.Giantsrole = nextcord.utils.get(bot.league.roles, name=Giantsname)
  bot.Broncosrole = nextcord.utils.get(bot.league.roles, name=Broncosname)
  bot.Jetsrole = nextcord.utils.get(bot.league.roles, name=Jetsname)
  bot.Billsrole = nextcord.utils.get(bot.league.roles, name=Billsname)
  bot.Washingtonrole = nextcord.utils.get(bot.league.roles, name=Washingtonname)
  bot.Panthersrole = nextcord.utils.get(bot.league.roles, name=Panthersname)
  bot.Ravensrole = nextcord.utils.get(bot.league.roles, name=Ravensname)
  bot.Saintsrole = nextcord.utils.get(bot.league.roles, name=Saintsname)
  bot.Patriotsrole = nextcord.utils.get(bot.league.roles, name=Patriotsname)
  bot.Falconsrole = nextcord.utils.get(bot.league.roles, name=Falconsname)
  bot.Coltsrole = nextcord.utils.get(bot.league.roles, name=Coltsname)
  bot.Cardinalsrole = nextcord.utils.get(bot.league.roles, name=Cardinalsname)
  bot.Ramsrole = nextcord.utils.get(bot.league.roles, name=Ramsname)
  bot.Bengalsrole = nextcord.utils.get(bot.league.roles, name=Bengalsname)
  bot.Titansrole = nextcord.utils.get(bot.league.roles, name=Titansname)
  bot.Texansrole = nextcord.utils.get(bot.league.roles, name=Texansname)
  bot.Chargersrole = nextcord.utils.get(bot.league.roles, name=Chargersname)
  bot.Jaguarsrole = nextcord.utils.get(bot.league.roles, name=Jaguarsname)
  bot.Lionsrole = nextcord.utils.get(bot.league.roles, name=Lionsname)
  bot.FranchiseOwner = nextcord.utils.get(bot.league.roles, name=FOname)
  bot.GeneralManager = nextcord.utils.get(bot.league.roles, name=GMname)
  bot.HeadCoach = nextcord.utils.get(bot.league.roles, name=HCname)
  bot.teams = [bot.Lionsrole,bot.Jaguarsrole,bot.Chargersrole, bot.Texansrole,bot.Titansrole,bot.Bengalsrole,bot.Ramsrole,bot.Cardinalsrole,bot.Coltsrole,bot.Falconsrole,bot.Patriotsrole,bot.Saintsrole,bot.Ravensrole,bot.Panthersrole,bot.Chiefsrole,bot.Falconsrole,bot.Billsrole,bot.Bearsrole,bot.Brownsrole,bot.Cowboysrole,bot.Broncosrole,bot.Packersrole,bot.Dolphinsrole,bot.Vikingsrole,bot.Giantsrole,bot.Jetsrole,bot.Raidersrole,bot.Eaglesrole,bot.Steelersrole,bot.ninersrole,bot.Seahawksrole,bot.Buccaneersrole,bot.Washingtonrole]

  await bot.change_presence(activity=nextcord.Game(name=f"To Buy this Bot, say /order. I am the #1 Fully Customizable Sign Bot in the Market | Created by Jinx"))
  print("BOT ACTIVATED!")

@bot.slash_command(name="order",description="Get the bot in your League",guild_ids=[db['Guild']])
async def order(interaction):
  author = interaction.user
  await interaction.response.defer(ephemeral=True)
  embed=nextcord.Embed(title="Order Assistant",color=db['Color'],description=f"If you would like to a Sign Bot, please join https://discord.gg/mffUyAmeQk and type /order again")
  embed.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await interaction.send(embed=embed,ephemeral=True)

@bot.slash_command(name="ban",description="Ban a user",guild_ids=[db['Guild']])
@cooldown(1,120,bucket=cooldowns.SlashBucket.author)
@application_checks.has_any_role(db['Adminrole'])
async def ban(interaction, user:Member, reason:str):
  author = interaction.user
  member = user 
  embed=nextcord.Embed(title="You have been banned",color=db['Color'],description=f"{member.mention}, you have been banned by {author.mention}\n **Reason:** {reason}")
  embed.set_thumbnail(url=modimage)
  embed.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await user.send(embed=embed)
  
  await user.ban(reason=reason)
  enforcements = bot.get_channel(db['EnforcementsChannel'])
  embed=nextcord.Embed(title="Member Banned",color=db['Color'],description=f"{member.mention} has been banned by {author.mention}\n **Reason:** {reason}")
  embed.set_thumbnail(url=modimage)
  embed.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await interaction.send(embed=embed)
  await enforcements.send(embed=embed)

@bot.slash_command(name="kick",description="Kick a user",guild_ids=[db['Guild']])
@application_checks.has_any_role(db['Adminrole'])
@cooldown(1,60,bucket=cooldowns.SlashBucket.author)
async def kick(interaction, user:Member, reason:str):
  author = interaction.user
  member = user 
  embed=nextcord.Embed(title="You have been kicked",color=db['Color'],description=f"{member.mention}, you have been kicked by {author.mention}\n **Reason:** {reason}")
  embed.set_thumbnail(url=modimage)
  embed.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await user.send(embed=embed)
  
  await interaction.guild.kick(user)
  enforcements = bot.get_channel(db['EnforcementsChannel'])
  embed=nextcord.Embed(title="Member Kicked",color=db['Color'],description=f"{member.mention} has been kicked by {author.mention}\n **Reason:** {reason}")
  embed.set_thumbnail(url=modimage)
  embed.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await interaction.send(embed=embed)
  await enforcements.send(embed=embed)

@bot.slash_command(name="unban",description="Unbans a user",guild_ids=[db['Guild']])
@application_checks.has_any_role(db['Adminrole'])
async def unban(interaction, userid:str):
  user = await bot.fetch_user(int(userid))
  member = user
  author = interaction.user
  await interaction.guild.unban(user)
  await interaction.response.defer(ephemeral=False)
  embed=nextcord.Embed(title="Member Unbanned",color=db['Color'],description=f"{member.mention} has been unbanned by {author.mention}")
  embed.set_thumbnail(url=modimage)
  embed.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await interaction.send(embed=embed)
  await enforcements.send(embed=embed)
  


@bot.slash_command(name="mute",description="Mute a User",guild_ids=[db['Guild']])
@application_checks.has_any_role(db['Ownerrole'],db['Modrole'],db['Adminrole'])
async def mute(interaction, user: Member,reason:str,time:str=SlashOption(name="time",required=True,choices={"1 Minute","5 Minutes","10 Minutes","1 Hour","1 Day","1 Week"})):
  await interaction.response.defer(ephemeral=False)
  enforcements = bot.get_channel(db['EnforcementsChannel'])
  user_id = user.id
  guild_id = interaction.guild.id
  member = user
  author = interaction.user
  timetext = time
  if timetext == "1 Minute":
    time_in_secs = "1m"
  elif timetext == "5 Minutes":
    time_in_secs = "5m"
  elif timetext == "10 Minutes":
    time_in_secs = "10m"
  elif timetext == "1 Hour":
    time_in_secs = "1h"
  elif timetext == "1 Day":
    time_in_secs = "1d"
  elif timetext == "1 Week":
    time_in_secs = "1w"
  time = humanfriendly.parse_timespan(time_in_secs)
  await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time))

  embed=nextcord.Embed(title="You have been muted",color=db['Color'],description=f"{member.mention}, you have been muted by {author.mention}\n **Reason:** {reason}\n **Duration:** {timetext}")
  embed.set_thumbnail(url=modimage)
  embed.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await member.send(embed=embed)
  
  embed=nextcord.Embed(title="Member Muted",color=db['Color'],description=f"{member.mention} has been muted by {author.mention}\n **Reason:** {reason}\n **Duration:** {timetext}")
  embed.set_thumbnail(url=modimage)
  embed.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await interaction.send(embed=embed)
  await enforcements.send(embed=embed)

  await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time))

@bot.slash_command(name="unmute",description="Unmute a User",guild_ids=[db['Guild']])
@application_checks.has_any_role(db['Ownerrole'],db['Modrole'],db['Adminrole'])
async def unmute(interaction, user: Member):
 enforcements = bot.get_channel(db['EnforcementsChannel'])
 member = user
 author = interaction.user
 await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=0))
 embed=nextcord.Embed(title="You have been muted",color=db['Color'],description=f"{member.mention}, you have been unmuted by {author.mention}")
 embed.set_thumbnail(url=modimage)
 embed.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
 embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
 await member.send(embed=embed)

 embed=nextcord.Embed(title="Member Unmuted",color=db['Color'],description=f"{member.mention} has been unmuted by {author.mention}")
 embed.set_thumbnail(url=modimage)
 embed.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
 embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
 await interaction.send(embed=embed)
 await enforcements.send(embed=embed)

@bot.slash_command(name="role",description="Removes/Adds a role to/from a user",guild_ids=[db['Guild']])
@application_checks.has_any_role(db['Ownerrole'],db['Modrole'],db['Adminrole'])
async def role(interaction, user: Member,role: Role, option:str=SlashOption(name="option",required=True,choices={"Add","Remove"})):
 enforcements = bot.get_channel(db['EnforcementsChannel'])
 member = user
 author = interaction.user

 if user.top_role < author.top_role:
   if role < author.top_role:
     if option == "Add":
       await member.add_roles(role)
       embed=nextcord.Embed(title="Role Added",color=db['Color'],description=f"{member.mention} has been given the {role.mention} role by {author.mention}")
       embed.set_thumbnail(url=modimage)
       embed.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
       embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
       await interaction.send(embed=embed)
       await enforcements.send(embed=embed)
     else:
       await member.remove_roles(role)
       embed=nextcord.Embed(title="Role Removed",color=db['Color'],description=f"{member.mention}'s {role.mention} role has been removed by {author.mention}")
       embed.set_thumbnail(url=modimage)
       embed.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
       embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
       await interaction.send(embed=embed)
       await enforcements.send(embed=embed)
   else:
      embed=nextcord.Embed(title="Role Error",color=db['Color'],description=f"You can only give/remove roles that are lower in hierarchy than you!")
      embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
      embed.set_thumbnail(url=errorimage)
      await interaction.send(embed=embed,ephemeral=True) 
 else:
  embed=nextcord.Embed(title="Role Error",color=db['Color'],description=f"You can only manage users roles who are on a lower rank than you!")
  embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
  embed.set_thumbnail(url=errorimage)
  await interaction.send(embed=embed,ephemeral=True)


@bot.slash_command(name="addroles",description="Finds the teams that haven't been made in the server roles and makes them automatically",guild_ids=[db['Guild']])
@application_checks.has_any_role(db['Ownerrole'])
async def addroles(interaction):
  await interaction.response.defer(ephemeral=True)
  guild = interaction.guild
  author = interaction.user
  embed=nextcord.Embed(title="Finding Roles",color=db['Color'],description=f"Scanning all the roles and making sure all 32 NFL Teams have been made")
  embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
  embed.set_thumbnail(url="https://images.squarespace-cdn.com/content/v1/5f0c301c93ea301f3c01c03d/1595443306627-3O8FNAKDGKCF3MBFCJGS/B4-icon-encore-search-data.gif")
  
  await interaction.followup.send(embed=embed)
  if not nextcord.utils.get(guild.roles,name="San Francisco 49ers"):
    role = await guild.create_role(name="San Francisco 49ers",color=0xaa0000,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Atlanta Falcons"):
    role = await guild.create_role(name="Atlanta Falcons",color=0xa71930,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Baltimore Ravens"):
    role = await guild.create_role(name="Baltimore Ravens",color=0x241773,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Buffalo Bills"):
    role = await guild.create_role(name="Buffalo Bills",color=0x00274d,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Carolina Panthers"):
    role = await guild.create_role(name="Carolina Panthers",color=0x0085ca,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Chicago Bears"):
    role = await guild.create_role(name="Chicago Bears",color=0xc83803,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Cincinnati Bengals"):
    role = await guild.create_role(name="Cincinnati Bengals",color=0xfb4f14,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Cleveland Browns"):
    role = await guild.create_role(name="Cleveland Browns",color=0xff3c00,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Dallas Cowboys"):
    role = await guild.create_role(name="Dallas Cowboys",color=0x00338d,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Denver Broncos"):
    role = await guild.create_role(name="Denver Broncos",color=0xFB4F14,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Detroit Lions"):
    role = await guild.create_role(name="Detroit Lions",color=0x0076B6,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Green Bay Packers"):
    role = await guild.create_role(name="Green Bay Packers",color=0x203731,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Indianapolis Colts"):
    role = await guild.create_role(name="Indianapolis Colts",color=0x002C5F,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Jacksonville Jaguars"):
    role = await guild.create_role(name="Jacksonville Jaguars",color=0xD7A22A,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Kansas City Chiefs"):
    role = await guild.create_role(name="Kansas City Chiefs",color=0xe31837,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Los Angeles Chargers"):
    role = await guild.create_role(name="Los Angeles Chargers",color=0x00ffed,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Los Angeles Rams"):
    role = await guild.create_role(name="Los Angeles Rams",color=0xb3995d,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Miami Dolphins"):
    role = await guild.create_role(name="Miami Dolphins",color=0x008e97,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Minnesota Vikings"):
    role = await guild.create_role(name="Minnesota Vikings",color=0x4f2683,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="New England Patriots"):
    role = await guild.create_role(name="New England Patriots",color=0x002244,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="New Orleans Saints"):
    role = await guild.create_role(name="New Orleans Saints",color=0xd3bc8d,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="New York Giants"):
    role = await guild.create_role(name="New York Giants",color=0x0b2265,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="New York Jets"):
    role = await guild.create_role(name="New York Jets",color=0x003f2d,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Las Vegas Raiders"):
    role = await guild.create_role(name="Las Vegas Raiders",color=0xa5acaf,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Philadelphia Eagles"):
    role = await guild.create_role(name="Philadelphia Eagles",color=0x004c54,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Pittsburgh Steelers"):
    role = await guild.create_role(name="Pittsburgh Steelers",color=0xFFB612,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Seattle Seahawks"):
    role = await guild.create_role(name="Seattle Seahawks",color=0x9be28,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Tampa Bay Buccaneers"):
    role = await guild.create_role(name="Tampa Bay Buccaneers",color=0xd50a0a,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Tennessee Titans"):
    role = await guild.create_role(name="Tampa Bay Buccaneers",color=0x4b92db,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  if not nextcord.utils.get(guild.roles,name="Washington Commanders"):
    role = await guild.create_role(name="Washington Commanders",color=0x773141,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*")
  embed=nextcord.Embed(title="Completed Checks",color=db['Color'],description=f"Completed the check! All 32 NFL Teams have been made! Hoewever some commands might still not work until you run the /resetbot command to reset the bot")
  embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
  embed.set_thumbnail(url="https://cliply.co/wp-content/uploads/2020/04/422004440_CHECKMARK_3D_ICON_400.png")
  
  await interaction.send(embed=embed)

@bot.slash_command(name="resetbot",description="Resets bot, sometimes fixes bugs",guild_ids=[db['Guild']])
@application_checks.has_any_role(db['Ownerrole'])
async def resetbot(interaction):
 author = interaction.user
 embed=nextcord.Embed(title="Bot Resetting",color=db['Color'],description=f"Please wait while i reset. Commands will not work for a couple seconds. *Please wait atleast 10 minutes before you run this command again or the bot will be overloaded and temporarily turned off).*")
 embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
 embed.set_thumbnail(url="https://media2.giphy.com/media/l5Ixyi91ENW1N2MyAc/giphy.gif")
 
 await interaction.send(embed=embed)

 os.system("clear")
 os.execv(sys.executable, ['python'] + sys.argv)

@bot.slash_command(name="namechange",description="Change the Bot's Name",guild_ids=[db['Guild']])
@application_checks.has_any_role(db['Ownerrole'])
async def namechange(interaction,name: str):
  await interaction.response.defer(ephemeral=True)
  try:
    await bot.user.edit(username=name)
    author = interaction.user
    embed=nextcord.Embed(title="Bot Name Changed",color=db['Color'],description=f"My name has been changed and will be seen shortly") 
    embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
    embed.set_thumbnail(url="https://cliply.co/wp-content/uploads/2020/04/422004440_CHECKMARK_3D_ICON_400.png")
    await interaction.followup.send(embed=embed,ephemeral=True)
  except:
    await interaction.followup.send("Either too many people have this name or you are changing the bot's name too fast!",ephemeral=True)


@bot.slash_command(name="pfpchange",description="Change the Bot's Profile Picutre",guild_ids=[db['Guild']])
@application_checks.has_any_role(db['Ownerrole'])
async def pfpchange(interaction,imageurl: str):
 await interaction.response.defer()
 async with aiohttp.ClientSession() as ses:
    async with ses.get(imageurl) as r:
     try:
       imgorgif = BytesIO(await r.read())
       bvalue = imgorgif.getvalue()
       await bot.user.edit(avatar=bvalue)
       await ses.close()
     except nextcord.HTTPException:
        await interaction.send(f"*Image Size too big!*",ephemeral=True)
 author = interaction.user
 embed=nextcord.Embed(title="Bot Avatar Changed",color=db['Color'],description=f"My avatar has been changed and will be seen shortly") 
 embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
 embed.set_thumbnial(url=imageurl)
 await interaction.followup.send(embed=embed)

@bot.slash_command(name="embedcolor",description="Change the color of embeds",guild_ids=[db['Guild']])
@application_checks.has_any_role(db['Ownerrole'])
async def embedcolor(interaction):
  author = interaction.user
  embed=nextcord.Embed(title="Select a Color",color=db['Color'],description=f"> 1. Transparent (Grey)\n > 2. Scarlet Red\n > 3. Sunrise Orange\n > 4. Electric Yellow\n > 5. Sand Gold\n > 6. Mint Green\n > 7. Electric Blue\n > 8. Royal Blue\n > 9. Royal Purple\n > 10. Flower Pink\n > 11. Midnight Black \n > 12. Snow White \n> 13. Metalic Grey")
  embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
  embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
  
  one = Button(label="1",style=ButtonStyle.blurple)
  two = Button(label="2",style=ButtonStyle.blurple)
  three = Button(label="3",style=ButtonStyle.blurple)
  four = Button(label="4",style=ButtonStyle.blurple)
  five = Button(label="5",style=ButtonStyle.blurple)
  six = Button(label="6",style=ButtonStyle.blurple)
  seven = Button(label="7",style=ButtonStyle.blurple)
  eight = Button(label="8",style=ButtonStyle.blurple)
  nine = Button(label="9",style=ButtonStyle.blurple)
  ten = Button(label="10",style=ButtonStyle.blurple)
  eleven = Button(label="11",style=ButtonStyle.blurple)
  twelve = Button(label="12",style=ButtonStyle.blurple)
  thirteen = Button(label="13",style=ButtonStyle.blurple)
  async def one_callback(interaction):
    db['Color'] = 0x2F3136
    embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'],description=f"The new embed background color has been set to *Transparent*")
    embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
    embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
    
    await interaction.send(embed=embed)
  async def two_callback(interaction):
   db['Color'] = 0xEB144C
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'],description=f"The new embed background color has been set to *Scarlet Red*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def three_callback(interaction):
   db['Color'] = 0xff9800
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'],description=f"The new embed background color has been set to *Sunrise Orange*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def four_callback(interaction):
   db['Color'] = 0xffeb3b
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'],description=f"The new embed background color has been set to *Electric Yellow*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def five_callback(interaction):
   db['Color'] = 0xFFE08A
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'],description=f"The new embed background color has been set to *Sandy Gold*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def six_callback(interaction):
   db['Color'] = 0x52ff60
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'],description=f"The new embed background color has been set to *Mint Green*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def seven_callback(interaction):
   db['Color'] = 0x00d5ff
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'],description=f"The new embed background color has been set to *Electric Blue*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def eight_callback(interaction):
   db['Color'] = 0x0008ff
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'],description=f"The new embed background color has been set to *Royal Blue*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def nine_callback(interaction):
   db['Color'] = 0x0008ff
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'],description=f"The new embed background color has been set to *Royal Purple*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def ten_callback(interaction):
   db['Color'] = 0xfb00ff
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'],description=f"The new embed background color has been set to *Flower Pink*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def eleven_callback(interaction):
   db['Color'] = 0x080008
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'],description=f"The new embed background color has been set to *Midnight Black*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def twelve_callback(interaction):
   db['Color'] = 0xf5f5f5
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'],description=f"The new embed background color has been set to *Snow White*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def thirteen_callback(interaction):
   db['Color'] = 0x2b2b2b
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'],description=f"The new embed background color has been set to *Metalic Grey*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  one.callback = one_callback
  two.callback = two_callback
  three.callback = four_callback
  four.callback = four_callback
  five.callback = five_callback
  six.callback = six_callback
  seven.callback = seven_callback
  eight.callback = eight_callback
  nine.callback = nine_callback
  ten.callback = ten_callback
  eleven.callback = eleven_callback
  twelve.callback = twelve_callback
  thirteen.callback = thirteen_callback
  myview = View(timeout=400)
  myview.add_item(one)
  myview.add_item(three)
  myview.add_item(four)
  myview.add_item(two)
  myview.add_item(five)
  myview.add_item(six) 
  myview.add_item(seven) 
  myview.add_item(eight)
  myview.add_item(nine)
  myview.add_item(ten)
  myview.add_item(eleven)
  myview.add_item(twelve)
  myview.add_item(thirteen)

  await interaction.send(embed=embed,ephemeral=True,view=myview)


@bot.slash_command(name="addemojis",guild_ids=[db['Guild']])
@application_checks.has_any_role(db['Ownerrole'])
async def addemojis(interaction, type:str=SlashOption(name="type",required=True,choices={"UFG Neon NFL"})):
  await interaction.response.defer(ephemeral=True)
  guild = interaction.guild
  author = interaction.user
  
  if type == "UFG Neon NFL":
    embed=nextcord.Embed(title="Confirmation Prompt",color=db['Color'],description=f"Are you sure you would like to add all 32 Neon NFL Emojis to the server? *Below is an example of what it would look like*")
    embed.set_image(url="https://cdn.discordapp.com/emojis/906372448201625640.webp?size=96&quality=lossless")
    yes = Button(label="Accept",emoji="✅",style=ButtonStyle.green)
    no = Button(label="Decline",emoji="❌",style=ButtonStyle.red)
    
    async def yes_callback(interaction):
      await interaction.response.edit_message(view=None)
      await interaction.send("*Beginning Emoji Creation*",ephemeral=True)
      number = 0 
      emojis = ["https://cdn.discordapp.com/emojis/933066081747238923.webp?size=96&quality=lossless",'https://cdn.discordapp.com/emojis/906372326407413841.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372448201625640.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372461812129842.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372538953764865.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372595434258453.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372656054554705.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372737562456124.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372783745957888.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372853614665779.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372910476832778.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372974121222224.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/943003615549849640.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373103087661136.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373160595775528.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373214207361135.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373284780728370.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373351180759042.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/933066320960946216.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373484496695367.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373539995729981.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373615627419659.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373682383954021.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373757055160370.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373816593313804.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373927805255711.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373995102871583.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906374091840294952.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906374154478030969.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906374232420798485.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906374326943641601.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/939966906834747402.webp?size=96&quality=lossless']
      names = ['ArizonaCardinals','AtlantaFalcons','BaltimoreRavens','BuffaloBills','CarolinaPanthers','ChicagoBears','CincinnatiBengals','ClevelandBrowns','DallasCowboys','DenverBroncos','DetroitLions','GreenBayPackers','HoustonTexans','IndianapolisColts','JacksonvilleJaguars','KansasCityChiefs','LasVegasRaiders','LosAngelesChargers','LosAngelesRams','MiamiDolphins','MinnesotaVikings','NewEnglandPatriots','NewOrleansSaints','NewYorkGiants','NewYorkJets','PhiladelphiaEagles','PittsburghSteelers','SanFrancisco49ers','SeattleSeahawks','TampaBayBuccaneers','TennesseeTitans','WashingtonCommanders']
      for emoji in emojis:
        name = names[number]
        number += 1
        url = emoji
        async with aiohttp.ClientSession() as ses:
          async with ses.get(url) as r:
            try:
              imgorgif = BytesIO(await r.read())
              bvalue = imgorgif.getvalue()
              if r.status in range(200,299):
               emoji = await guild.create_custom_emoji(name=name,image=bvalue)
               await interaction.send(f"*Made {str(emoji)} and named it `{name}`*",delete_after=1)
               await ses.close()
              else:
                await interaction.send(f"didnt work {r.status}")
            except discord.HTTPException:
               await interaction.send(f"*{name} emoji size is too big!*",ephemeral=True)
    async def no_callback(interaction):
      await interaction.response.edit_message(view=None)
    yes.callback = yes_callback
    no.callback = no_callback
    myview = View(timeout=400)
    myview.add_item(yes)
    myview.add_item(no)
    
    msgembed = await interaction.followup.send(embed=embed,view=myview,ephemeral=True)

@bot.slash_command(
  name="notification",
  description="Enable/Disable Notifications for certain events",
  guild_ids=[db['Guild']],
)
async def notification(
  interaction,
  option: str = SlashOption(name="option",
                            description="Please Select a Option Above!",
                            required=True,
                            choices={"Pickups","Events","League"})
  ):
  print("2")
  member = interaction.user
  print(member.name)
  if option == 'Pickups':
     Pickups = nextcord.utils.get(bot.league.roles, id=db['Pickups'])
     if Pickups in member.roles:
       await member.remove_roles(Pickups)
       embed=nextcord.Embed(title="Notifications Updated",color=db['Color'],description=f"You no longer have the {Pickups.mention} role!")
       embed.set_thumbnail(url=notificationimage)
       await interaction.send(embed=embed,ephemeral=True) 
     else:
       await member.add_roles(Pickups)
       embed=nextcord.Embed(title="Notifications Updated",color=db['Color'],description=f"You now have the {Pickups.mention} role!")
       embed.set_thumbnail(url=notificationimage)
       await interaction.send(embed=embed,ephemeral=True) 
       
  elif option == "Events":
    Events = nextcord.utils.get(bot.league.roles, id=db['Events'])
    if Events in member.roles:
       await member.remove_roles(Events)
       embed=nextcord.Embed(title="Notifications Updated",color=db['Color'],description=f"You no longer have the {Events.mention} role!")
       embed.set_thumbnail(url=notificationimage)
       await interaction.send(embed=embed,ephemeral=True) 
    else:
       await member.add_roles(Events)
       embed=nextcord.Embed(title="Notifications Updated",color=db['Color'],description=f"You now have the {Events.mention} role!")
       embed.set_thumbnail(url=notificationimage)
       await interaction.send(embed=embed,ephemeral=True) 
       
  elif option == "League":
    League = nextcord.utils.get(bot.league.roles, id=db['League'])
    if League in member.roles:
       await member.remove_roles(League)
       embed=nextcord.Embed(title="Notifications Updated",color=db['Color'],description=f"You no longer have the {League.mention} role!")
       embed.set_thumbnail(url=notificationimage)
       await interaction.send(embed=embed,ephemeral=True) 
    else:
       await member.add_roles(League)
       embed=nextcord.Embed(title="Notifications Updated",color=db['Color'],description=f"You now have the {Pickups.mention} role!")
       embed.set_thumbnail(url=notificationimage)
       await interaction.send(embed=embed,ephemeral=True) 
    

@bot.slash_command(name="help",description="View Information about the bot",
  guild_ids=[db['Guild']],
)
async def help(interaction):
   await interaction.response.defer(ephemeral=True)
   total = 0 
   commands = bot.get_all_application_commands()
   for command in commands:
     total += 1
     
   embed1=nextcord.Embed(title="🏠 Home",description=f"\n> `Version` 6.0 Premium\n > `Command Count` {str(total)}\n> `Want your Own Sign Bot or Need Support?` Join https://discord.gg/UDVWrz75Xj and contact Jinx\n",color=db['Color'])
   embed1.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)

   embed2=nextcord.Embed(title="🎨 Customization Commands",color=db['Color'],description="**Requires Owner Role**\n `/addemojis <type>` - Adds team emoji packs such as the ones in UFG\n `/addroles` - Checks which team roles aren't made and makes them\n `/embedcolor` - Change the color of embeds \n `/Setimage <image link>` - Changes the image that appears at the bottom of embeds *Say None to have no bottom image* \n `pfpchange <image link>` - Changes the bots profile picture\n `namechange <name>` - Changes the bots name")

   embed2.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)

   embed3=nextcord.Embed(title="💸 Transaction Commands",description="`Gametimes` - /gametime teamagainst time \n `Trading` - /trade <useroffered> <userreceived> \n `Signing` - /sign <user> \n `Offering` - /offer <user> \n `Releasing` - /release <user> \n `Promoting` - /promote <HC/GM> <user> \n `Demoting` - /demote <HC/GM> <user> \n `Demanding` - /demand \n `Posting To FreeAgency` - /lfp <info> \n**Notes:**\n\n would mean slash command not the prefix. \nMust be Franchise Owner/General Manager/Head Coach to do transaction commands, must be franchise owner to promote and demote General Managers and Head Coaches.\n Offers automatically expire after 1 hour",color=db['Color'])
   embed3.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)

   embed4=nextcord.Embed(title="📘 General Commands",description="`/Roster <team>` - Shows you a teams roster \n `/Members <role>` - Shows you the member list of a role \n `/Templates <TC/League>` - Gives you free templates\n `/find <Teamname> <Position>` - Shows you the HC/GM/FO of a team (replace position with HC/GM/FO) \n `/ringcheck <user>` - shows you if a player has rings.\n `/Compare <team1> <team2name>` - Compares the roster between 2 teams \n `/av <user>` - shows you a users avatar\n `/LeagueInfo` - Shows you the information for this league \n `/Profile <user>` - Shows you a users League Profile and rewards \n `/8ball <question>` - Rolls a magic 8ball\n `/membercount` - Shows the servers membercount",color=db['Color'])
   embed4.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)

   embed5=nextcord.Embed(title="🔰 League Management Commands",description="**League Management Commands** \n `/Check <Rosters>` - Displays sizes of all rosters in the League \n `/Franchise <Verification>` - Ensures no bots are signed and that there aren't any players on multiple teams \n `/reset <demands>` - Resets everyones demands back to 0\n `/roster <team>` - Shows a roster for a team \n `/Opening <team>` - Notifies players that a team is open for claiming\n `/FO <List>` - Shows a complete list of all the Franchise Owners \n `/available <teams>` - Shows a list of teams without players \n `/FO <Check>` - displays teams with players but no Franchise Owner\n `/whitelist <team> Transactions` - Allows the team to do transaction commands __Transactions still must be turned off or all teams will be able to do Transactions__\n`/unwhitelist <team> transactions` - Removes the team from the whitelist\n**Team Management Commands**\n`/Relocate <oldteam> <newteam>` - Transfers all the players from one team to another \n `/Swap <team1> <team2>` - relocates each player on both teams to the other team\n`/disband <team>` - Releases all players from a team __Auto demotes Franchise Owners, Head Coaches, General Managers__\n`/purge <team>` - Same as disband except it will not effect the franchise owner\n `/appoint <user> <team>` - Roles the mentioned user as the francise owner of the selected team __will replace the old Franchise Owner__ \n `/suspend <user> <season number> <week number> <reason>` Example: suspend @user 1 3 cheating in game] would suspend them until season 1 week 3\n`/unsuspend <user>` - unsuspends a user\n `/suspensions` - shows a list of all suspensions\n `/warn` - generates the warning prompt ",color=db['Color'])   
   embed5.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
