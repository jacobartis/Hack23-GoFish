import discord
from discord.utils import get
from discord.ext import commands
import servo 
bot = commands.Bot(command_prefix=["\\","~"])
##command to move servo
@commands.has_role("moderator")
@bot.command(name="feed",help = "moves the servo to feed the fish")
async def feedfish(ctx):
    await ctx.channel.send("feeding time has begun")
    feedingtime()
    await ctx.channel.send("feeding time has come to an end")
##command to turn on the lights
##@commands.has_role("moderator")
##@bot.command(name="light",help = "toggles the lights")
##async def flashbang(ctx):
##    #run the type script code
##    
    
bot.run('NzM5MjIxNDIyMjQ4OTUxODcw.GeB8kM.Ns9YZyN1SuGBDPk1gUPdbK_C9pbh-3cBVA_Fx0')
