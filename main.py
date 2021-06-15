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
   
