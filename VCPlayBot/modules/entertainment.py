import requests
from pyrogram import Client
from VCPlayBot.config import BOT_USERNAME
from VCPlayBot.helpers.filters import command

@Client.on_message(command(["asupan", f"asupan@{BOT_USERNAME}"]))
async def asupan(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("https://te.legra.ph/file/9ee01453fc404013fabf1.jpg")


@Client.on_message(command(["wibu", f"wibu@{BOT_USERNAME}"]))
async def wibu(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/wibu").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("`https://te.legra.ph/file/e5023a7fe6b5d116c6326.mp4`")


@Client.on_message(command(["chika", f"chika@{BOT_USERNAME}"]))
async def chika(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("https://te.legra.ph/file/aa370d5d0abf3e9d629bc.mp4")


@Client.on_message(command(["truth", f"truth@{BOT_USERNAME}"]))
async def truth(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/truth").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("https://te.legra.ph/file/e5023a7fe6b5d116c6326.mp4")


@Client.on_message(command(["dare", f"dare@{BOT_USERNAME}"]))
async def dare(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/dare").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("https://t.me/DARKAMANSUPPORT")
