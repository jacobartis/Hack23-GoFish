import discord
from discord.utils import get
from discord.ext import commands
import Servo
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=["\\","~"],intents = intents)

##command to move servo
@commands.has_role("moderator")
@bot.command(name="feed",help = "moves the servo to feed the fish")
async def feedfish(ctx, freq):
    await ctx.channel.send("feeding time has begun, feeding ",freq," times!")
    Servo.feeding_time(freq)
    await ctx.channel.send("feeding time has come to an end")
##command to turn on the lights
##@commands.has_role("moderator")
##@bot.command(name="light",help = "toggles the lights")
##async def flashbang(ctx):
##    #run the type script code
##    

#Reads the token from token.txt and runs the corisponding bot
token_f = open("token.txt","r")
bot.run(token_f.readline())
token_f.close()