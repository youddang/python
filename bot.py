import discord
import asyncio

client = discord.Client()
token = ''

@client.event()
async def on_message(msg):

    print(f"{msg.channel} {msg.author} - {msg.content}")
    if "탄압" in msg.content:
        await msg.delete()
        await msg.channel.send(f"{msg.author.mention} 님이 모함하셨습니다.")

    if msg.content.startswith("$clear "):
        purge_number = msg.content.replace("$clear ", "")
        check_purge_number = purge_number.isdigit()

        if check_purge_number == True:
            await msg.channel.purge(limit = int(purge_number) + 1)
        else:
            await msg.channel.send("정수 값을 넣어주세요.")