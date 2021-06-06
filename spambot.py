import discord

client = discord.Client()
BOT_TOKEN = ''
bad_words = ["nig", "nikg", "nuig", "njg", "nijg", "niq", "njq", "nijq", "nuiq"]

@client.event
async def on_message(message):
    for i in range(len(bad_words)):
        if bad_words[i] in message.content:
            for j in range(5):
                await message.author.send("Okay, you are going to stop using n word")
            for k in range(1):
                await message.author.send("https://media.discordapp.net/attachments/808116483665952789/809935266524561498/caption-10.gif")
                
print('Bot is running')

client.run(BOT_TOKEN)
