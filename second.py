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
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
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

#RUN THIS TO RESET EVERYTHING AND START BOT

# db['Color'] = {}               
# db['Ownerrole'] = {}           
# db['Managerrole'] = {}         
# db['Modrole'] = {}             
# db['Adminrole'] = {}           
# db['League'] = {}              
# db['Pickups'] = {}             
# db['Events'] = {}              
# db['Suspended'] = {}           
# db['3 Demands'] = {}           
# db['2 Demands'] = {}           
# db['1 Demands'] = {}           
# db['No Demands'] = {}                    
# db['TransactionsWhitelist'] = {}    
# db['EnforcementsChannel'] = {}      
# db['botsban'] = {}                
# db['PlayerDetection'] = {}        
# db['OwnerDetection'] = {}         
# db['demandsenable'] = {}         
# db['ghostpingtoggle'] = {}       
# db['rostermax'] = {}              
# db['channeldefensetoggle'] = {}    
# db['transactionsenable'] = {}     
# db['FreeAgency'] = {}            
# db['GametimesChannel'] = {}       
# db['TransactionsChannel'] = {}    
# db['VerdictsChannel'] = {}      
# db['NoticesChannel'] = {}      
# db['AlertsChannel'] = {}
# db['Season'] = {}
# db['Week'] = {}
# db['Guilds'] = [968256394073616394]


teamnames = ['Kansas City Chiefs','Minnesota Vikings','Dallas Cowboys','Green Bay Packers','San Francisco 49ers','Tampa Bay Buccaneers','Philadelphia Eagles','Pittsburgh Steelers','Seattle Seahawks','Chicago Bears','Cleveland Browns','Miami Dolphins','Las Vegas Raiders','Denver Broncos','New York Jets','New York Giants','Buffalo Bills','Washington Commanders','Carolina Panthers','Baltimore Ravens','New Orleans Saints','New England Patriots','Atlanta Falcons','Indianapolis Colts','Arizona Cardinals','Los Angeles Rams','Cincinnati Bengals','Tennessee Titans','Houston Texans','Los Angeles Chargers','Jacksonville Jaguars','Detroit Lions']
#college teams 32
teamnames.extend(["Alabama Crimson Tide","Auburn Tigers","Boston College Eagles","Buffalo Bulls","Cincinnati Bearcats","Clemson Tigers","Colorado Buffaloes","Georgia Bulldogs","Indian Hoosiers","Iowa Hawkeyes","Kansas Jayhawks","Miami Hurricanes","Michigan State Spartans","Michigan Wolverines","Nebraska Cornhuskers","North Carolina Tar Heels","Norte Dame","Ohio State Buckeyes","Oklahoma Sooners","Oregon Ducks","Penn State Nittany Lions","Pittsburgh Panthers","Rutgers Scarlet Knights","Stanford Cardinals","Tennessee Volunteers","Texas Longhorns","USC Trojans","Utah Utes","Virginia Tech","West Virginia Mountaineers","Wisconsin Badgers","Maryland Terrapins"])
HCname = "Head Coach" 
FOname = "Franchise Owner" 
GMname = "General Manager" 

Intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!@#@#ddsdnvniriubeiwfneie", intents=Intents, case_insensitive = True) 
bot.remove_command('help')

errorimage = "https://media0.giphy.com/media/xT9Igpm06uM5OJ5lVS/giphy.gif?cid=6c09b9521t3cf41euzffzfoa700ihvi4wpjj6t53czdkpoj5&rid=giphy.gif&ct=s"
utilitiesimage = "https://miro.medium.com/max/1400/1*44799UW8y4KGlJb36fTD7Q.gif"
notificationimage = "https://cdn.dribbble.com/users/2514055/screenshots/5538470/__.gif"
verdictimage = "https://media.baamboozle.com/uploads/images/197603/1624188519_136711.gif"
modimage = "https://monshare.io/wp-content/uploads/2020/03/Shield-high.gif"

@bot.event
async def on_ready():
  await bot.change_presence(activity=nextcord.Game(name="⚡ Best Multi-Server Sign Bot, Say /Order to purchase!"))
  print("BOT ACTIVATED!")
  
@bot.event
async def on_guild_remove(guild):
  if guild.channel.guild.id in db['Guilds']:
    pass
  else:
    return
  try:
   backgroundcolor = int(db['Color'][f"{guild.id}"])
  except:
   backgroundcolor = 0x2F3136
  user = bot.get_user(813815467952701450)
  embed=nextcord.Embed(title="Bot Removed",color=backgroundcolor,description="The bot has been removed from a server. To free up storage space say /stopguild")
  embed.add_field(name="Server Name:",value=guild.name)
  embed.add_field(name="Server ID:",value=guild.id)
  await user.send(embed=embed)

@bot.event
async def on_guild_join(guild):
  try:
   backgroundcolor = int(db['Color'][f"{guild.id}"])
  except:
   backgroundcolor = 0x2F3136
  if guild.id in db['Guilds']:
    status = "✅ Paid"
  else:
    status = "⚠️ You have not paid for the bot yet, Commands will not load for your server (To purchase the bot please join [Our Support Server](https://discord.gg/mffUyAmeQk))"
  embed=nextcord.Embed(title="Thank you for adding the #1 Sign Bot!",color=backgroundcolor,description="To set me up wait for the slash commands to load (about a minute or so) and say /debug")
  embed.add_field(name="Server Status:",value=status)
  embed.add_field(name="Support",value="If you have questions, bugs, suggestions, or need to purchase another bot please join [Our Support Server](https://discord.gg/mffUyAmeQk)")
  randomchannel = random.choice(guild.text_channels)
  try:
   await randomchannel.send(embed=embed)
   await randomchannel.send(guild.owner.mention)
  except:
    await guild.owner.send(embed=embed)

@bot.slash_command(name="order",description="Get the bot in your League",guild_ids=db['Guilds'])
async def order(interaction):
  try:
   backgroundcolor = int(db['Color'][f"{interaction.guild.id}"])
  except:
   backgroundcolor = 0x2F3136
  author = interaction.user
  await interaction.response.defer(ephemeral=True)
  embed=nextcord.Embed(title="Order Assistant",color=backgroundcolor,description=f"If you would like to order your own Bot, Have Questions, Have suggestions, or would like to report a bug, please join [Our Support Server](https://discord.gg/mffUyAmeQk) and type /order again")
  embed.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await interaction.send(embed=embed,ephemeral=True)


@bot.slash_command(name="embed",description="Send a Embed",guild_ids=db['Guilds'])
async def embed(interaction,title:str=SlashOption(name="title",required=False),description:str=SlashOption(name="description",required=False),footer:str=SlashOption(name="footer",required=False)):
  try:
   backgroundcolor = int(db['Color'][f"{interaction.guild.id}"])
  except:
   backgroundcolor = 0x2F3136
  try:
   Managerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Adminrole'][f"{interaction.guild.id}"]))
   Managerrole2 = nextcord.utils.get(interaction.guild.roles, id=int(db['Modrole'][f"{interaction.guild.id}"]))
   Managerrole3 = nextcord.utils.get(interaction.guild.roles, id=int(db['Ownerrole'][f"{interaction.guild.id}"]))
   Managerrole4 = nextcord.utils.get(interaction.guild.roles, id=int(db['Managerrole'][f"{interaction.guild.id}"]))
   if Managerrole not in  interaction.user.roles and Managerrole2 not in interaction.user.roles and Managerrole3 not in interaction.user.roles and Managerrole4 not in interaction.user.roles:
     embed=nextcord.Embed(title="Command Error", description=f"*Only Users with these Select roles can use this command:*\n {Managerrole.mention},{Managerrole2.mention},{Managerrole3},{Managerrole4.mention}", color=backgroundcolor)
     embed.set_thumbnail(url=errorimage)
     await interaction.send(embed=embed,ephemeral=True)
     return
  except:
   embed=nextcord.Embed(title="Command Error", description=f"*The Admin/Mod/Owner and/or Manager role has not been set, say /debug to figure out how to set it.*", color=backgroundcolor)
   embed.set_thumbnail(url=errorimage)
   await interaction.send(embed=embed,ephemeral=True)
   return 
  if title == None:
    title = "Title Not Set"
  if description == None:
    description = "Description Not Set"
  
  embed = nextcord.Embed(title=title,description=description,color=backgroundcolor)
  if footer != None:
    embed.set_footer(text=footer)
  await interaction.send(embed=embed)

@bot.slash_command(name="ban",description="Ban a user",guild_ids=db['Guilds'])
@cooldown(1,120,bucket=cooldowns.SlashBucket.author)
async def ban(interaction, user:Member, reason:str):
  try:
   backgroundcolor = int(db['Color'][f"{interaction.guild.id}"])
  except:
   backgroundcolor = 0x2F3136
  try:
   Managerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Adminrole'][f"{interaction.guild.id}"]))
   if Managerrole not in  interaction.user.roles:
     embed=nextcord.Embed(title="Command Error", description=f"*Only Users with these Select roles can use this command:*\n {Managerrole.mention}", color=backgroundcolor)
     embed.set_thumbnail(url=errorimage)
     await interaction.send(embed=embed,ephemeral=True)
     return
  except:
   embed=nextcord.Embed(title="Command Error", description=f"*The Admin role has not been set, say /debug to figure out how to set it.*", color=backgroundcolor)
   embed.set_thumbnail(url=errorimage)
   await interaction.send(embed=embed,ephemeral=True)
   return 
    
  author = interaction.user
  member = user 
  embed=nextcord.Embed(title="You have been banned",color=backgroundcolor,description=f"{member.mention}, you have been banned by {author.mention}\n **Reason:** {reason}")
  embed.set_thumbnail(url=modimage)
  embed.set_author(name=f"{interaction.guild.name} Moderation Services",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await user.send(embed=embed)
  
  await user.ban(reason=reason)
  enforcements = bot.get_channel(db['EnforcementsChannel'][f"{interaction.guild.id}"])
  embed=nextcord.Embed(title="Member Banned",color=backgroundcolor,description=f"{member.mention} has been banned by {author.mention}\n **Reason:** {reason}")
  embed.set_thumbnail(url=modimage)
  embed.set_author(name=f"{interaction.guild.name} Moderation Services",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await interaction.send(embed=embed)
  await enforcements.send(embed=embed)

@bot.slash_command(name="kick",description="Kick a user",guild_ids=db['Guilds'])
@cooldown(1,60,bucket=cooldowns.SlashBucket.author)
async def kick(interaction, user:Member, reason:str):
  try:
   backgroundcolor = int(db['Color'][f"{interaction.guild.id}"])
  except:
   backgroundcolor = 0x2F3136
  try:
   Managerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Adminrole'][f"{interaction.guild.id}"]))
   if Managerrole not in  interaction.user.roles:
     embed=nextcord.Embed(title="Command Error", description=f"*Only Users with these Select roles can use this command:*\n {Managerrole.mention}", color=backgroundcolor)
     embed.set_thumbnail(url=errorimage)
     await interaction.send(embed=embed,ephemeral=True)
     return
  except:
   embed=nextcord.Embed(title="Command Error", description=f"*The Admin role has not been set, say /debug to figure out how to set it.*", color=backgroundcolor)
   embed.set_thumbnail(url=errorimage)
   await interaction.send(embed=embed,ephemeral=True)
   return 
    
  author = interaction.user
  member = user 
  embed=nextcord.Embed(title="You have been kicked",color=backgroundcolor,description=f"{member.mention}, you have been kicked by {author.mention}\n **Reason:** {reason}")
  embed.set_thumbnail(url=modimage)
  embed.set_author(name=f"{interaction.guild.name} Moderation Services",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await user.send(embed=embed)
  
  await interaction.guild.kick(user)
  enforcements = bot.get_channel(db['EnforcementsChannel'][f"{interaction.guild.id}"])
  embed=nextcord.Embed(title="Member Kicked",color=backgroundcolor,description=f"{member.mention} has been kicked by {author.mention}\n **Reason:** {reason}")
  embed.set_thumbnail(url=modimage)
  embed.set_author(name=f"{interaction.guild.name} Moderation Services",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await interaction.send(embed=embed)
  await enforcements.send(embed=embed)

@bot.slash_command(name="unban",description="Unbans a user",guild_ids=db['Guilds'])
async def unban(interaction, userid:str):
  try:
   backgroundcolor = int(db['Color'][f"{interaction.guild.id}"])
  except:
   backgroundcolor = 0x2F3136
  try:
   Managerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Adminrole'][f"{interaction.guild.id}"]))
   if Managerrole not in  interaction.user.roles:
     embed=nextcord.Embed(title="Command Error", description=f"*Only Users with these Select roles can use this command:*\n {Managerrole.mention}", color=backgroundcolor)
     embed.set_thumbnail(url=errorimage)
     await interaction.send(embed=embed,ephemeral=True)
     return
  except:
   embed=nextcord.Embed(title="Command Error", description=f"*The Admin role has not been set, say /debug to figure out how to set it.*", color=backgroundcolor)
   embed.set_thumbnail(url=errorimage)
   await interaction.send(embed=embed,ephemeral=True)
   return 
    
  user = await bot.fetch_user(int(userid))
  member = user
  author = interaction.user
  await interaction.guild.unban(user)
  await interaction.response.defer(ephemeral=False)
  embed=nextcord.Embed(title="Member Unbanned",color=backgroundcolor,description=f"{member.mention} has been unbanned by {author.mention}")
  embed.set_thumbnail(url=modimage)
  embed.set_author(name=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await interaction.send(embed=embed)
  await enforcements.send(embed=embed)
  


@bot.slash_command(name="mute",description="Mute a User",guild_ids=db['Guilds'])
async def mute(interaction, user: Member,reason:str,time:str=SlashOption(name="time",required=True,choices={"1 Minute","5 Minutes","10 Minutes","1 Hour","1 Day","1 Week"})):
  try:
   backgroundcolor = int(db['Color'][f"{interaction.guild.id}"])
  except:
   backgroundcolor = 0x2F3136
  try:
   Modrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Modrole'][f"{interaction.guild.id}"]))
   Managerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Managerrole'][f"{interaction.guild.id}"]))
   Ownerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Ownerrole'][f"{interaction.guild.id}"]))
   if Managerrole not in  interaction.user.roles and Modrole not in interaction.user.roles and Ownerrole not in interaction.user.roles:
     embed=nextcord.Embed(title="Command Error", description=f"*Only Users with these Select roles can use this command:*\n {Modrole.mention},{Managerrole.mention}.{Ownerrole.mention}", color=backgroundcolor)
     embed.set_thumbnail(url=errorimage)
     await interaction.send(embed=embed,ephemeral=True)
     return
  except:
   embed=nextcord.Embed(title="Command Error", description=f"*The Moderator, Admin, and/or Owner role has not been set, say /debug to figure out how to set it.*", color=backgroundcolor)
   embed.set_thumbnail(url=errorimage)
   await interaction.send(embed=embed,ephemeral=True)
   return 
  await interaction.response.defer(ephemeral=False)
  enforcements = bot.get_channel(db['EnforcementsChannel'][f"{interaction.guild.id}"])
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

  embed=nextcord.Embed(title="You have been muted",color=backgroundcolor,description=f"{member.mention}, you have been muted by {author.mention}\n **Reason:** {reason}\n **Duration:** {timetext}")
  embed.set_thumbnail(url=modimage)
  embed.set_author(name=f"{interaction.guild.name} Moderation Services",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await member.send(embed=embed)
  
  embed=nextcord.Embed(title="Member Muted",color=backgroundcolor,description=f"{member.mention} has been muted by {author.mention}\n **Reason:** {reason}\n **Duration:** {timetext}")
  embed.set_thumbnail(url=modimage)
  embed.set_author(name=f"{interaction.guild.name} Moderation Services",icon_url=interaction.guild.icon.url)
  embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
  await interaction.send(embed=embed)
  await enforcements.send(embed=embed)

  await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time))

@bot.slash_command(name="unmute",description="Unmute a User",guild_ids=db['Guilds'])
async def unmute(interaction, user: Member):
 try:
   backgroundcolor = int(db['Color'][f"{interaction.guild.id}"])
 except:
   backgroundcolor = 0x2F3136
 try:
   Modrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Modrole'][f"{interaction.guild.id}"]))
   Managerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Managerrole'][f"{interaction.guild.id}"]))
   Ownerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Ownerrole'][f"{interaction.guild.id}"]))
   if Managerrole not in  interaction.user.roles and Modrole not in interaction.user.roles and Ownerrole not in interaction.user.roles:
     embed=nextcord.Embed(title="Command Error", description=f"*Only Users with these Select roles can use this command:*\n {Modrole.mention},{Managerrole.mention}.{Ownerrole.mention}", color=backgroundcolor)
     embed.set_thumbnail(url=errorimage)
     await interaction.send(embed=embed,ephemeral=True)
     return
 except:
   embed=nextcord.Embed(title="Command Error", description=f"*The Moderator, Admin and/or Owner role has not been set, say /debug to figure out how to set it.*", color=backgroundcolor)
   embed.set_thumbnail(url=errorimage)
   await interaction.send(embed=embed,ephemeral=True)
   return 
 enforcements = bot.get_channel(db['EnforcementsChannel'][f"{interaction.guild.id}"])
 
 member = user
 author = interaction.user
 await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=0))
 embed=nextcord.Embed(title="You have been muted",color=backgroundcolor,description=f"{member.mention}, you have been unmuted by {author.mention}")
 embed.set_thumbnail(url=modimage)
 embed.set_author(name=f"{interaction.guild.name} Moderation Services",icon_url=interaction.guild.icon.url)
 embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
 await member.send(embed=embed)

 embed=nextcord.Embed(title="Member Unmuted",color=backgroundcolor,description=f"{member.mention} has been unmuted by {author.mention}")
 embed.set_thumbnail(url=modimage)
 embed.set_author(name=f"{interaction.guild.name} Moderation Services",icon_url=interaction.guild.icon.url)
 embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
 await interaction.send(embed=embed)
 await enforcements.send(embed=embed)

@bot.slash_command(name="role",description="Removes/Adds a role to/from a user",guild_ids=db['Guilds'])
async def role(interaction, user: Member,role: Role, option:str=SlashOption(name="option",required=True,choices={"Add","Remove"})):
 try:
   backgroundcolor = int(db['Color'][f"{interaction.guild.id}"])
 except:
   backgroundcolor = 0x2F3136
 try:
   Modrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Modrole'][f"{interaction.guild.id}"]))
   Managerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Managerrole'][f"{interaction.guild.id}"]))
   Ownerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Ownerrole'][f"{interaction.guild.id}"]))
   if Managerrole not in  interaction.user.roles and Modrole not in interaction.user.roles and Ownerrole not in interaction.user.roles:
     embed=nextcord.Embed(title="Command Error", description=f"*Only Users with these Select roles can use this command:*\n {Modrole.mention},{Managerrole.mention}.{Ownerrole.mention}", color=backgroundcolor)
     embed.set_thumbnail(url=errorimage)
     await interaction.send(embed=embed,ephemeral=True)
     return
 except:
   embed=nextcord.Embed(title="Command Error", description=f"*The Moderator, Admin and/or Owner role has not been set, say /debug to figure out how to set it.*", color=backgroundcolor)
   embed.set_thumbnail(url=errorimage)
   await interaction.send(embed=embed,ephemeral=True)
   return 
 
 enforcements = bot.get_channel(db['EnforcementsChannel'][f"{interaction.guild.id}"])
 member = user
 author = interaction.user

 if user.top_role < author.top_role:
   if role < author.top_role:
     if option == "Add":
       await member.add_roles(role)
       embed=nextcord.Embed(title="Role Added",color=backgroundcolor,description=f"{member.mention} has been given the {role.mention} role by {author.mention}")
       embed.set_thumbnail(url=modimage)
       embed.set_author(name=f"{interaction.guild.name} Moderation Services",icon_url=interaction.guild.icon.url)
       embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
       await interaction.send(embed=embed)
       await enforcements.send(embed=embed)
     else:
       await member.remove_roles(role)
       embed=nextcord.Embed(title="Role Removed",color=backgroundcolor,description=f"{member.mention}'s {role.mention} role has been removed by {author.mention}")
       embed.set_thumbnail(url=modimage)
       embed.set_author(name=f"{interaction.guild.name} Moderation Services",icon_url=interaction.guild.icon.url)
       embed.set_footer(icon_url=author.display_avatar.url,text=f"{author.name}#{author.discriminator}")
       await interaction.send(embed=embed)
       await enforcements.send(embed=embed)
   else:
      embed=nextcord.Embed(title="Role Error",color=backgroundcolor,description=f"You can only give/remove roles that are lower in hierarchy than you!")
      embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
      embed.set_thumbnail(url=errorimage)
      await interaction.send(embed=embed,ephemeral=True) 
 else:
  embed=nextcord.Embed(title="Role Error",color=backgroundcolor,description=f"You can only manage users roles who are on a lower rank than you!")
  embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
  embed.set_thumbnail(url=errorimage)
  await interaction.send(embed=embed,ephemeral=True)


@bot.slash_command(name="addroles",description="Finds the teams that haven't been made in the server roles and makes them automatically",guild_ids=db['Guilds'])
async def addroles(interaction):
  await interaction.response.defer(ephemeral=True)
  try:
   backgroundcolor = int(db['Color'][f"{interaction.guild.id}"])
  except:
   backgroundcolor = 0x2F3136
  try:
   Managerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Managerrole'][f"{interaction.guild.id}"]))
   Ownerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Ownerrole'][f"{interaction.guild.id}"]))
   if Managerrole not in  interaction.user.roles and Ownerrole not in interaction.user.roles:
     embed=nextcord.Embed(title="Command Error", description=f"*Only Users with these Select roles can use this command:*\n {Managerrole.mention}.{Ownerrole.mention}", color=backgroundcolor)
     embed.set_thumbnail(url=errorimage)
     await interaction.send(embed=embed,ephemeral=True)
     return
  except:
   embed=nextcord.Embed(title="Command Error", description=f"*The Moderator, Admin and/or Owner role has not been set, say /debug to figure out how to set it.*", color=backgroundcolor)
   embed.set_thumbnail(url=errorimage)
   await interaction.send(embed=embed,ephemeral=True)
   return 
    
  guild = interaction.guild
  author = interaction.user
  embed=nextcord.Embed(title="Finding Roles",color=backgroundcolor,description=f"Scanning all the roles and making sure all 32 NFL Teams have been made")
  embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
  embed.set_thumbnail(url="https://emoji.gg/assets/emoji/6943_Verified.gif")
  
  await interaction.followup.send(embed=embed)
  if not nextcord.utils.get(guild.roles,name="San Francisco 49ers"):
    role = await guild.create_role(name="San Francisco 49ers",color=0xaa0000,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Arizona Cardinals"):
    role = await guild.create_role(name="Arizona Cardinals",color=0xff0026,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Houston Texans"):
    role = await guild.create_role(name="Houston Texans",color=0x03202F,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="New York Jets"):
    role = await guild.create_role(name="New York Jets",color=0x125740,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Atlanta Falcons"):
    role = await guild.create_role(name="Atlanta Falcons",color=0xa71930,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Baltimore Ravens"):
    role = await guild.create_role(name="Baltimore Ravens",color=0x241773,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Buffalo Bills"):
    role = await guild.create_role(name="Buffalo Bills",color=0x00274d,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Carolina Panthers"):
    role = await guild.create_role(name="Carolina Panthers",color=0x0085ca,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Chicago Bears"):
    role = await guild.create_role(name="Chicago Bears",color=0xc83803,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Cincinnati Bengals"):
    role = await guild.create_role(name="Cincinnati Bengals",color=0xfb4f14,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Cleveland Browns"):
    role = await guild.create_role(name="Cleveland Browns",color=0xff3c00,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Dallas Cowboys"):
    role = await guild.create_role(name="Dallas Cowboys",color=0x00338d,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Denver Broncos"):
    role = await guild.create_role(name="Denver Broncos",color=0xFB4F14,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Detroit Lions"):
    role = await guild.create_role(name="Detroit Lions",color=0x0076B6,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Green Bay Packers"):
    role = await guild.create_role(name="Green Bay Packers",color=0x203731,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Indianapolis Colts"):
    role = await guild.create_role(name="Indianapolis Colts",color=0x002C5F,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Jacksonville Jaguars"):
    role = await guild.create_role(name="Jacksonville Jaguars",color=0xD7A22A,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Kansas City Chiefs"):
    role = await guild.create_role(name="Kansas City Chiefs",color=0xe31837,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Los Angeles Chargers"):
    role = await guild.create_role(name="Los Angeles Chargers",color=0x00ffed,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Los Angeles Rams"):
    role = await guild.create_role(name="Los Angeles Rams",color=0xb3995d,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Miami Dolphins"):
    role = await guild.create_role(name="Miami Dolphins",color=0x008e97,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Minnesota Vikings"):
    role = await guild.create_role(name="Minnesota Vikings",color=0x4f2683,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="New England Patriots"):
    role = await guild.create_role(name="New England Patriots",color=0x002244,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="New Orleans Saints"):
    role = await guild.create_role(name="New Orleans Saints",color=0xd3bc8d,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="New York Giants"):
    role = await guild.create_role(name="New York Giants",color=0x0b2265,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="New York Jets"):
    role = await guild.create_role(name="New York Jets",color=0x003f2d,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Las Vegas Raiders"):
    role = await guild.create_role(name="Las Vegas Raiders",color=0xa5acaf,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Philadelphia Eagles"):
    role = await guild.create_role(name="Philadelphia Eagles",color=0x004c54,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Pittsburgh Steelers"):
    role = await guild.create_role(name="Pittsburgh Steelers",color=0xFFB612,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Seattle Seahawks"):
    role = await guild.create_role(name="Seattle Seahawks",color=0x9be28,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Tampa Bay Buccaneers"):
    role = await guild.create_role(name="Tampa Bay Buccaneers",color=0xD50A0A,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Tennessee Titans"):
    role = await guild.create_role(name="Tennessee Titans",color=0x4b92db,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  if not nextcord.utils.get(guild.roles,name="Washington Commanders"):
    role = await guild.create_role(name="Washington Commanders",color=0x773141,mentionable=False)
    await interaction.send(f"*I Created {role.mention} because it wasn't made already*",delete_after=1)
  embed=nextcord.Embed(title="Completed Checks",color=backgroundcolor,description=f"Completed the check! All 32 NFL Teams Roles have been made!")
  embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
  embed.set_thumbnail(url="https://emoji.gg/assets/emoji/6943_Verified.gif")
  
  await interaction.send(embed=embed)

@bot.slash_command(name="embedcolor",description="Change the color of embeds",guild_ids=db['Guilds'])
async def embedcolor(interaction):
  try:
   backgroundcolor = int(db['Color'][f"{interaction.guild.id}"])
  except:
   backgroundcolor = 0x2F3136
  try:
   Managerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Managerrole'][f"{interaction.guild.id}"]))
   Ownerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Ownerrole'][f"{interaction.guild.id}"]))
   if Managerrole not in  interaction.user.roles and Ownerrole not in interaction.user.roles:
     embed=nextcord.Embed(title="Command Error", description=f"*Only Users with these Select roles can use this command:*\n {Managerrole.mention}.{Ownerrole.mention}", color=backgroundcolor)
     embed.set_thumbnail(url=errorimage)
     await interaction.send(embed=embed,ephemeral=True)
     return
  except:
   embed=nextcord.Embed(title="Command Error", description=f"*The Manager and/or Owner role has not been set, say /debug to figure out how to set it.*", color=backgroundcolor)
   embed.set_thumbnail(url=errorimage)
   await interaction.send(embed=embed,ephemeral=True)
   return 
    
  author = interaction.user
  embed=nextcord.Embed(title="Select a Color",color=backgroundcolor,description=f"> 1. Transparent (Grey)\n > 2. Scarlet Red\n > 3. Sunrise Orange\n > 4. Electric Yellow\n > 5. Sand Gold\n > 6. Mint Green\n > 7. Electric Blue\n > 8. Royal Blue\n > 9. Royal Purple\n > 10. Flower Pink\n > 11. Midnight Black \n > 12. Snow White \n> 13. Metalic Grey")
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
    db['Color'][f"{interaction.guild.id}"] = 0x2F3136
    embed=nextcord.Embed(title="Color Changed Succesfully",color=int(db['Color'][f"{interaction.guild.id}"]),description=f"The new embed background color has been set to *Transparent*")
    embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
    embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
    
    await interaction.send(embed=embed)
  async def two_callback(interaction):
   db['Color'][f"{interaction.guild.id}"] = 0xff0019
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'][f"{interaction.guild.id}"],description=f"The new embed background color has been set to *Scarlet Red*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def three_callback(interaction):
   db['Color'][f"{interaction.guild.id}"] = 0xff9800
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'][f"{interaction.guild.id}"],description=f"The new embed background color has been set to *Sunrise Orange*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def four_callback(interaction):
   db['Color'][f"{interaction.guild.id}"] = 0xffeb3b
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'][f"{interaction.guild.id}"],description=f"The new embed background color has been set to *Electric Yellow*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def five_callback(interaction):
   db['Color'][f"{interaction.guild.id}"] = 0xFFE08A
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'][f"{interaction.guild.id}"],description=f"The new embed background color has been set to *Sandy Gold*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def six_callback(interaction):
   db['Color'][f"{interaction.guild.id}"] = 0x52ff60
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'][f"{interaction.guild.id}"],description=f"The new embed background color has been set to *Mint Green*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def seven_callback(interaction):
   db['Color'][f"{interaction.guild.id}"] = 0x00d5ff
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'][f"{interaction.guild.id}"],description=f"The new embed background color has been set to *Electric Blue*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def eight_callback(interaction):
   db['Color'][f"{interaction.guild.id}"] = 0x0008ff
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'][f"{interaction.guild.id}"],description=f"The new embed background color has been set to *Royal Blue*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def nine_callback(interaction):
   db['Color'][f"{interaction.guild.id}"] = 0x0008ff
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'][f"{interaction.guild.id}"],description=f"The new embed background color has been set to *Royal Purple*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def ten_callback(interaction):
   db['Color'][f"{interaction.guild.id}"] = 0xfb00ff
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'][f"{interaction.guild.id}"],description=f"The new embed background color has been set to *Flower Pink*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def eleven_callback(interaction):
   db['Color'][f"{interaction.guild.id}"] = 0x080008
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'][f"{interaction.guild.id}"],description=f"The new embed background color has been set to *Midnight Black*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def twelve_callback(interaction):
   db['Color'][f"{interaction.guild.id}"] = 0xf5f5f5
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'][f"{interaction.guild.id}"],description=f"The new embed background color has been set to *Snow White*")
   embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.display_avatar.url)
   embed.set_thumbnail(url="https://media.giphy.com/media/CocQnEN254LJK/giphy.gif")
   
   await interaction.send(embed=embed)
  async def thirteen_callback(interaction):
   db['Color'][f"{interaction.guild.id}"] = 0x2b2b2b
   embed=nextcord.Embed(title="Color Changed Succesfully",color=db['Color'][f"{interaction.guild.id}"],description=f"The new embed background color has been set to *Metalic Grey*")
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
  myview.add_item(two)
  myview.add_item(three)
  myview.add_item(four)
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


@bot.slash_command(name="addemojis",guild_ids=db['Guilds'])
async def addemojis(interaction, type:str=SlashOption(name="type",required=True,choices={"Neon NFL"})):
  try:
   backgroundcolor = int(db['Color'][f"{interaction.guild.id}"])
  except:
   backgroundcolor = 0x2F3136
  try:
   Managerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Managerrole'][f"{interaction.guild.id}"]))
   Ownerrole = nextcord.utils.get(interaction.guild.roles, id=int(db['Ownerrole'][f"{interaction.guild.id}"]))
   if Managerrole not in  interaction.user.roles and Ownerrole not in interaction.user.roles:
     embed=nextcord.Embed(title="Command Error", description=f"*Only Users with these Select roles can use this command:*\n {Managerrole.mention}.{Ownerrole.mention}", color=backgroundcolor)
     embed.set_thumbnail(url=errorimage)
     await interaction.send(embed=embed,ephemeral=True)
     return
  except:
   embed=nextcord.Embed(title="Command Error", description=f"*The Manager and/or Owner role has not been set, say /debug to figure out how to set it.*", color=backgroundcolor)
   embed.set_thumbnail(url=errorimage)
   await interaction.send(embed=embed,ephemeral=True)
   return 
  

  await interaction.response.defer(ephemeral=True)
  guild = interaction.guild
  author = interaction.user
  
  if type == "Neon NFL":
    embed=nextcord.Embed(title="Confirmation Prompt",color=backgroundcolor,description=f"Are you sure you would like to add all 32 Neon NFL Emojis to the server? *Below is an example of what it would look like*")
    embed.set_image(url="https://cdn.discordapp.com/emojis/906372448201625640.webp?size=96&quality=lossless")
    yes = Button(label="Accept",emoji="✅",style=ButtonStyle.green)
    no = Button(label="Decline",emoji="❌",style=ButtonStyle.red)
    
    async def yes_callback(interaction):
      await interaction.response.edit_message(view=None)
      await interaction.send("*Beginning Emoji Creation*",ephemeral=True)
      number = 0 
      emojis = ["https://cdn.discordapp.com/emojis/933066081747238923.webp?size=96&quality=lossless",'https://cdn.discordapp.com/emojis/906372326407413841.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372448201625640.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372461812129842.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372538953764865.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372595434258453.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372656054554705.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372737562456124.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372783745957888.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372853614665779.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372910476832778.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906372974121222224.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/943003615549849640.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373103087661136.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373160595775528.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373214207361135.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373284780728370.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373351180759042.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/933066320960946216.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373484496695367.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373539995729981.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373615627419659.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373682383954021.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373757055160370.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373816593313804.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373927805255711.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906373995102871583.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906374091840294952.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906374154478030969.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906374232420798485.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/906374326943641601.webp?size=96&quality=lossless','https://cdn.discordapp.com/emojis/939966906834747402.webp?size=96&quality=lossless']
      names = ['ArizonaCardinals','AtlantaFalcons','BaltimoreRavens','BuffaloBills','CarolinaPanthers','ChicagoBears','CincinnatiBengals','ClevelandBrowns','DallasCowboys','DenverBroncos','Det... (1 KB left)
message.txt
51 KB
