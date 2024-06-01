# from pyrogram import Client ,filters , emoji
from pyrogram import Client
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)






api_id =19900466 
api_hash = 'fc393ce306361ef2bb938ec8d2aa84fc'
bot_token = '5414065076:AAH5RsguSf0OYmgRX8a2LREWidsIRPgbBbk'


app = Client("my_account", api_id=api_id, api_hash=api_hash,  bot_token=bot_token)



@app.on_message()
async def main(client,message):
    await app.send_message(message.chat.id, "Hi")
    with app:
        print(message)
        # Send a message, Markdown is enabled by default
        await app.send_message(message.caht.id, "Hi there! I'm using **Pyrogram**")
    await main()


app.run()
