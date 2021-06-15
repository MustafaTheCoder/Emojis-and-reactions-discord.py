import discord
from discord.ext import commands

client = commands.Bot(command_prefix="-")
client.remove_command("help")

async def ch_pr():
    await client.wait_until_ready()
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(
        type=discord.ActivityType.watching,
        name=f"{len(client.guilds)} Servers | -help"))


client.loop.create_task(ch_pr())


@client.event
async def on_ready():
    print("Bot is ready!")



@client.command()
async def Hello(ctx):
    await ctx.send("Hi!")





@client.group(invoke_without_command=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def help(ctx):
    em = discord.Embed(
        title="__**Help Command**__",
        description="Your Description Here.", color=ctx.author.color)

    em.add_field(name="Option(1)", value="Value(1)")
    em.add_field(name="Option(2)", value="Value(2)")
    em.add_field(name="Option(3)", value="Value(3)")
    em.add_field(name="Option(4)", value="Value(4)")

    await ctx.send(embed=em)

@help.command()
async def test(ctx):
    await ctx.send("Success!")







@client.command()
async def test(ctx):
    await ctx.send("<:swag_kek:846442757542248487>") #Your emoji id here.
    #This lines send the emoji.


@client.event
async def on_message(msg):
    if "-help" in msg.content: #Checks if the content under the msg is equal to -help so that it can react on it.
        await msg.add_reaction("<a:check_mark:847021556638810123>") #Your reaction emoji id here | sends your reaction.

    await client.process_commands(msg) #This line is important dont forget to write it or else it wont work! 
    #What this line does is it process this event of checking the msg that we send so that it can react only on it and also process the help real command.
    

















client.run("ODUyMjQzODQxODA4OTkwMjU4.YMD_7Q.7MlVsumyG1sI2hTlbBQ7YjtyOYY")