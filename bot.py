import discord
import asyncio
import datetime

client = discord.Client()
token = ''
now = datetime.datetime.now()
time = f"{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초"


@client.event
async def on_message(msg):

    print(f"{msg.channel} {msg.author} - {msg.content}")
    if "" in msg.content:
        await msg.delete()
        await msg.channel.send(f"{msg.author.mention} 님이 모함하셨습니다.")
    if "" in msg.content:
        await msg.delete()
        await msg.channel.send(f"{msg.author.mention} 님이 기만하셨습니다.")
    if "test" in msg.content:
        await msg.delete()

    if msg.content.startswith("$clear "):
        purge_number = msg.content.replace("$clear ", "")
        check_purge_number = purge_number.isdigit()

        if check_purge_number == True:
            await msg.channel.purge(limit = int(purge_number) + 1)
        else:
            await msg.channel.send("정수 값을 넣어주세요.")
# @client.event
# async def on_message_delete(message):
#     channel = client.get_channel(input_channel_id)
#     embed = discord.Embed(title=f"삭제됨", description=f"유저 : {message.author.mention} 채널 : {message.channel.mention}", color=0xFF0000)
#     embed.add_field(name="삭제된 내용", value=f"내용 : {message.content}", inline=False)
#     embed.set_footer(text=f"{message.guild.name} | {time}")
#     await channel.send(embed=embed)

client.run(token)
