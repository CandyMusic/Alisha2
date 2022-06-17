from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    OWNER_USERNAME,   
)


@Client.on_callback_query(filters.regex("cb_start"))
async def start_op(_, query: CallbackQuery):
    await query.answer("Bot Started")
    await query.edit_message_text(
              f"""**Hello, Welcome {message.from_user.mention()}\n
I am powerful easy to use TeleGram Super Bot. I can play high quality and unbreakable music in your group voice chat. Just add me and promote with needed powers.\n
Use Inline buttons for more !!
For Help : @AlishaSupport**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✚ Gʀᴏᴜᴘ Mᴇ Lᴇ Jᴀᴏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton("👤 Dᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("📢 Sᴀᴜʀᴄᴇ", url=f"https://github.com/CandyMusic/Alisha2")
                ],[
                    InlineKeyboardButton("📨 Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/AlishaSupport"),
                    InlineKeyboardButton("📨 Uᴘᴅᴀᴛᴇs", url=f"https://t.me/Pubglovers_Shayri_lovers")
                ],[
                    InlineKeyboardButton("🔍 How To Use? Commands", callback_data="cb_cmd")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cb_cmd"))
async def cbcmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**🤖 Normal Bot Commands :-

» /play - (song name) 
» /skip - Skip the Song
» /end - Stop Playing Music
» /pause - Pause the track
» /resume - Resumes the Track
» /mute - Mute the Assistant 
» /search - (song name)



⚙ Some Extra Commands :-

» /ping - Shows the Ping Status
» /start - Starts the Bot
» /id - Get the ID
» /repo - Get the source code 
» /rmd - Clean all the downloads
» /clean - Clean the Storage
» /gcast - broadcast your message 


🌀 Powered By : @VeNom_Hai_HuM**""",
    )

