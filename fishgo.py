import discord
from discord.utils import get
from discord.ext import commands
import Servo
import auto_feeder
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

##command to add a time to auto feeder
@commands.has_role("moderator")
@bot.command(name="add_feed_time",help = "adds a time for the feeder to automaticly trigger")
async def add_feed_time(ctx, time:str):
    print(time.split(","))
    try:
        feed_times = open("auto_feed_times.txt","a")
        new_time = []
        for x in time.split(","):
            new_time.append(int(x))
        print(new_time)
        feed_times.write("\n"+str(new_time))
        feed_times.close()

    except:
        await ctx.channel.send("something went wrong")

##command to print all auto fed times
@commands.has_role("moderator")
@bot.command(name="feed_times",help = "shows all auto feed times")
async def add_feed_time(ctx):
    await ctx.channel.send("current auto feed times:")
    for x in open("auto_feed_times.txt").readlines():
        await ctx.channel.send(x.strip())

#Reads the token from token.txt and runs the corisponding bot
token_f = open("token.txt","r")
bot.run(token_f.readline())
token_f.close()