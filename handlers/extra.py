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


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text("**Tʜᴀɴᴋs Fᴏʀ Aᴅᴅɪɴɢ Mᴇ Iɴ Uʀ Gʀᴘ ❤️ Nᴏᴡ Pʀᴏᴍᴏᴛᴇ Mᴇ ᴀs Aᴅᴍɪɴ Fᴏʀ Pʟᴀʏɪɴɢ Sᴏɴɢs☺️!!**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ Dᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://github.com/CandyMusic/Alisha2")
                ],[
                    InlineKeyboardButton("🖤 Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/AlishaSupport"),
                    InlineKeyboardButton("❤️ Uᴘᴅᴀᴛᴇs", url=f"https://t.me/Pubglovers_Shayri_lovers")
                  ],
            ]
        ),
    )
