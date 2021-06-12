import discord
from discord.ext import commands 

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
   activity = discord.Game(name="do %help", type=3)
   await bot.change_presence(status=discord.Status.online, activity=activity)
   print('Bot Is Ready')

#ping#
@bot.command()
async def ping(ctx):
  await ctx.send(f'pong! {round(bot.latency * 1000)}ms', delete_after=10)
  await ctx.message.delete()
  
#sup#
@bot.command()
async def sup(ctx):
  await ctx.send('sup')

#kick
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason='No reason provided.'):
  await member.send(f'You have been **kicked** from {member.guild.name} for \"{reason}\".')
  await member.kick(reason=reason)
  await ctx.send(f'User {member} has been kicked.')


@kick.error
async def on_error(ctx, error):
 if isinstance(error, commands.CommandInvokeError):
  error = error.original
 if isinstance(error, commands.MissingPermissions):
        await ctx.send("you dont have permissions to run this command", delete_after=10)
        await ctx.message.delete()



@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    """Bans a user"""
    if reason == None:
        await ctx.send(f"Woah {ctx.author.mention}, Make sure you provide a reason!")
    else:
        messageok = f'You have been **banned** from {ctx.guild.name} for {reason}.'
        await member.send(messageok)
        await member.ban(reason=reason)
        await ctx.send(f'banned {member.mention}')


@ban.error
async def on_error(ctx, error):
 if isinstance(error, commands.CommandInvokeError):
  error = error.original
 if isinstance(error, commands.MissingPermissions):
        await ctx.send("you dont have permissions to run this command", delete_after=10)
        await ctx.message.delete()




@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
   banned_users = await ctx.guild.bans()
   member_name, member_discriminator = member.split('#')

   for ban_entry in banned_users:
      user = ban_entry.user

      if (user.name, user.discriminator) == (member_name, member_discriminator):
         await ctx.guild.unban(user)
         await ctx.send (f'unbanned {user.mention}')
         return




@ban.error
async def on_error(ctx, error):
 if isinstance(error, commands.CommandInvokeError):
  error = error.original
 if isinstance(error, commands.MissingPermissions):
        await ctx.send("you dont have permissions to run this command", delete_after=10)
        await ctx.message.delete()
#suggestions command
@bot.command()
async def suggestion(ctx):
  await ctx.send('Go to the suggestion channel to put a suggestion!', delete_after=10)
  await ctx.message.delete()




#say command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, message: str):
  await ctx.send(message)
  await ctx.message.delete()

@say.error
async def on_error(ctx, error):
 if isinstance(error, commands.CommandInvokeError):
  error = error.original
 if isinstance(error, commands.MissingPermissions):
        await ctx.send("you dont have permissions to run this command", delete_after=5)








#embed command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def embed(ctx, message: str):
  embed = discord.Embed(title=message, colour=discord.Colour.red())
  await ctx.send(embed=embed)
  await ctx.message.delete()
  

@embed.error
async def on_error(ctx, error):
 if isinstance(error, commands.CommandInvokeError):
  error = error.original
 if isinstance(error, commands.MissingPermissions):
        await ctx.send("you dont have permissions to run this command", delete_after=5)
 

bot.run('ODUyODA2ODk2MzQ2NzI2NDAw.YMMMUA.W7E_KaefJCvFoMLJ2ErPxwh4fmQ')


