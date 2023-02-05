import discord
from discord.utils import get
from discord.ext import commands
from ast import literal_eval
import threading
import Servo
import auto_feeder
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=["\\","~"],intents = intents)

#Creates a thread to run the auto feeder in parallel
auto_feeder_thread = threading.Thread(target=auto_feeder.start_check)
auto_feeder_thread.start()

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

#command to turn on the lights
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
    try:
        #Checks the input are correct
        assert(len(time.split(","))==3)
        assert(int(time.split(",")[0])<24 and int(time.split(",")[0])>=0)
        assert(int(time.split(",")[1])<60 and int(time.split(",")[1])>=0)
        assert(int(time.split(",")[2])<60 and int(time.split(",")[2])>=0)

        #Opens the auto feed file, formats the input and write to file
        
        new_time = []
        for x in time.split(","):
            new_time.append(int(x))
        
        with open("auto_feed_times.txt","r") as feed_times:
            for x in feed_times.readlines():
                if new_time == literal_eval(x.strip()):
                    await ctx.channel.send(f"{new_time} is already present on the auto feed schedule!")
                    return
        
        with  open("auto_feed_times.txt","a") as feed_times:
            feed_times.write("\n"+str(new_time))

        await ctx.channel.send(f"added {new_time} to auto feed")
    
    except:
        await ctx.channel.send("error! please put in form 'add_feed_time hour,minute,second'")

##command to print all auto fed times
@commands.has_role("moderator")
@bot.command(name="feed_times",help = "shows all auto feed times")
async def feed_times(ctx):
    await ctx.channel.send("current auto feed times:")
    for x in open("auto_feed_times.txt").readlines():
        if x.strip() != "":
            await ctx.channel.send(x.strip())

##command to print all auto fed times
@commands.has_role("moderator")
@bot.command(name="delete_feed_time",help = "deletes a time on the auto feed timetable")
async def delete_feed_time(ctx, time:str):
    try:
        #Checks the input are correct
        assert(len(time.split(","))==3)
        assert(int(time.split(",")[0])<24 and int(time.split(",")[0])>=0)
        assert(int(time.split(",")[1])<60 and int(time.split(",")[1])>=0)
        assert(int(time.split(",")[2])<60 and int(time.split(",")[2])>=0)

        #Opens the auto feed file, formats the input and write to file
        
        new_time = []
        for x in time.split(","):
            new_time.append(int(x))
        
        #Copies current feed times file
        lines = []
        with open("auto_feed_times.txt","r") as feed_times:
            lines = feed_times.readlines()
        
        #Clears the file and adds back lines not equal to the given value
        with open("auto_feed_times.txt","w") as feed_times:
            for line in lines:
                if new_time != literal_eval(line.strip()):
                    feed_times.write(line)
        await ctx.channel.send(f"{time} removed from the auto feed timetable")

    except:
        await ctx.channel.send("error! please put in form 'delete_feed_time hour,minute,second'")

##command to clear all auto feed times
@commands.has_role("moderator")
@bot.command(name="clear_feed_times",help = "deletes all current auto feed times")
async def add_feed_time(ctx, time:str):
    with open("auto_feed_times.txt","w") as feed_times:
        await ctx.channel.send("Auto feed times have been cleared")

#Reads the token from token.txt and runs the corisponding bot
token_f = open("token.txt","r")
bot.run(token_f.readline())
token_f.close()

