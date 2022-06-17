import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    OWNER_USERNAME,   
)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
     await message.reply_photo(
        photo=f"https://telegra.ph//file/7ee458e4a36161a036392.jpg",
        caption=f"""**Hᴇʏ ʙᴀʙʏ,ɪ'ᴍ ǫᴜᴇᴇɴ ᴀʟɪsʜᴀ\n🥀ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ 🎶 ʙᴏᴛ ʙᴀsᴇᴅ\n 🥀 ᴏɴ 💫ᴘʏᴛʜᴏɴ 🌎 ғᴇᴇʟ ❤️ ɴᴏ ʟᴀɢ  \n ғᴀsᴛ 🎧 ᴍᴜsɪᴄ.    \n 🥀𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 = [Aʙʜɪᴍᴀɴʏᴜ Sɪɴɢʜ Rᴀɴᴀᴡᴀᴛ](https://t.me/Venom_Hai_Hum)
        
        
Fᴏʀ ᴀɴʏ ʜᴇʟᴘ ᴅᴍ ᴍʏ ᴏᴡɴᴇʀ   🥀[Aʙʜɪᴍᴀɴʏᴜ Sɪɴɢʜ Rᴀɴᴀᴡᴀᴛ](https://t.me/VeNom_Hai_HuM)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✚ Gʀᴏᴜᴘ ᴍᴇ ʟᴇ ᴊᴀᴏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton("👤 Dᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/VeNom_Hai_HuM"),
                    InlineKeyboardButton("⚙️ Sᴜᴀʀᴄᴇ ", url=f"https://github.com/CandyMusic/Alisha2")
                ],[
                    InlineKeyboardButton("📨 Sᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/AlishaSupport"),
                    InlineKeyboardButton("📨 Uᴘᴅᴀᴛᴇs", url=f"https://t.me/Pubglovers_Shayri_lovers")
                ],[
                    InlineKeyboardButton("🔍  Hᴏᴡ ᴛᴏ ᴜsᴇ", callback_data="cb_cmd")
                ],
            ]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("**× I am Alive ×**\n\n@VeNom_Hai_HuM 📡")


@Client.on_message(command(["repo"]) & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text("`Click on the Button given below to Get the Bot Source Code.`",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ Sᴀᴜʀᴄᴇ ", url=f"https://github.com/CandyMusic/Alisha2")
                ]
            ]
        ),
    )
