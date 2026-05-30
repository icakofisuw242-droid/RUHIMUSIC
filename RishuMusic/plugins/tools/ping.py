from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaVideo, CallbackQuery

from RishuMusic import app
from RishuMusic.core.call import SACHIN
from RishuMusic.utils import bot_sys_stats
from RishuMusic.utils.decorators.language import language
from RishuMusic.utils.inline import supp_markup, close_markup
from config import BANNED_USERS, PING_IMG_URL, SUPPORT_CHAT


@app.on_message(filters.command("ping", prefixes=["/"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await SACHIN.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
