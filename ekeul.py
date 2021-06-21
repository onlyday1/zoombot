import discord
import openpyxl

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("자하유튜브 구독")
    await client.change_presence(status=discord.Status.online)


@client.event
async def on_message(message):
    if message.content.startswith("!회의"):
        await message.channel.send("에클님의 줌주소 : ```765 993 3870```")
        await message.channel.send("에클님의 줌 비번 : ```zahacute``` ")


        

client.run("ODU2MzgxNzU5Mjg5MDMyNzI0.YNANqg.MM0cywjUJojfFase13yfRpTDMms")