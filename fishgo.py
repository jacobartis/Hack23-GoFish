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
    
    #Checks the freq is an int
    try:
        assert(int(freq))

        await ctx.channel.send("feeding time has begun, feeding")
        Servo.feeding_time(int(freq))
        await ctx.channel.send("feeding time has come to an end")
    except:
        await ctx.channel.send("incorrect feed command, please put in form '~feed value' where value is a number or blank")
#Handles the user not inputing a message
@feedfish.error
async def feedfisherror(ctx, error):
    await ctx.channel.send("feeding time has begun, feeding")
    Servo.feeding_time(5)
    await ctx.channel.send("feeding time has come to an end")

##command to turn on the lights
@commands.has_role("moderator")
@bot.command(name="light",help = "toggles the lights")
async def flashbang(ctx):
    x = Servo.flashbang()
    if x.status_code == 200:
        await ctx.channel.send("flash bang out!")
    else:
        await ctx.channel.send("flash bang failed")

##command to turn on the lights
@commands.has_role("moderator")
@bot.command(name="add_auto_time",help = "adds a time for the feeder to automaticly trigger")
async def add_auto_time(ctx, time:str):
    try:
        feed_times = open("auto_feed_times.txt")
        new_time = []
        for x in time.split(","):
            new_time.append(x)
        feed_times.write(str(new_time))
    except:
        await ctx.channel.send("something went wrong")

#Reads the token from token.txt and runs the corisponding bot
token_f = open("token.txt","r")
bot.run(token_f.readline())
token_f.close()