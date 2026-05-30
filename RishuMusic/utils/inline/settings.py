from typing import Union

from pyrogram.types import InlineKeyboardButton


def setting_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["ST_B_1"], callback_data="AU"),
            InlineKeyboardButton(text=_["ST_B_2"], callback_data="PM"),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_4"], callback_data="VM"),
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons

def audio_quality_markup(
    _,
    LOW: Union[bool, str] = None,
    MEDIUM: Union[bool, str] = None,
    HIGH: Union[bool, str] = None,
    STUDIO: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_17"].format("✅") if LOW == True else _["ST_B_17"].format("")
                ),
                callback_data="LOW",
            ),
            InlineKeyboardButton(
                text=(
                    _["ST_B_18"].format("✅")
                    if MEDIUM == True
                    else _["ST_B_18"].format("")
                ),
                callback_data="MEDIUM",
            ),
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_19"].format("✅")
                    if HIGH == True
                    else _["ST_B_19"].format("")
                ),
                callback_data="HIGH",
            ),
            InlineKeyboardButton(
                text=(
                    _["ST_B_20"].format("✅")
                    if STUDIO == True
                    else _["ST_B_20"].format("")
                ),
                callback_data="STUDIO",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def video_quality_markup(
    _,
    SD_360p: Union[bool, str] = None,
    SD_480p: Union[bool, str] = None,
    HD_720p: Union[bool, str] = None,
    FHD_1080p: Union[bool, str] = None,
    QHD_2K: Union[bool, str] = None,
    UHD_4K: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_21"].format("✅")
                    if SD_360p == True
                    else _["ST_B_21"].format("")
                ),
                callback_data="SD_360p",
            ),
            InlineKeyboardButton(
                text=(
                    _["ST_B_22"].format("✅")
                    if SD_480p == True
                    else _["ST_B_22"].format("")
                ),
                callback_data="SD_480p",
            ),
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_23"].format("✅")
                    if HD_720p == True
                    else _["ST_B_23"].format("")
                ),
                callback_data="HD_720p",
            ),
            InlineKeyboardButton(
                text=(
                    _["ST_B_24"].format("✅")
                    if FHD_1080p == True
                    else _["ST_B_24"].format("")
                ),
                callback_data="FHD_1080p",
            ),
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_25"].format("✅")
                    if QHD_2K == True
                    else _["ST_B_25"].format("")
                ),
                callback_data="QHD_2K",
            ),
            InlineKeyboardButton(
                text=(
                    _["ST_B_26"].format("✅")
                    if UHD_4K == True
                    else _["ST_B_26"].format("")
                ),
                callback_data="UHD_4K",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def vote_mode_markup(_, current, mode: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text="Vᴏᴛɪɴɢ ᴍᴏᴅᴇ ➜", callback_data="VOTEANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_5"] if mode == True else _["ST_B_6"],
                callback_data="VOMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text="-2", callback_data="FERRARIUDTI M"),
            InlineKeyboardButton(
                text=f"ᴄᴜʀʀᴇɴᴛ : {current}",
                callback_data="ANSWERVOMODE",
            ),
            InlineKeyboardButton(text="+2", callback_data="FERRARIUDTI A"),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def auth_users_markup(_, status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text=_["ST_B_7"], callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_8"] if status == True else _["ST_B_9"],
                callback_data="AUTH",
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_1"], callback_data="AUTHLIST"),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(text=_["ST_B_10"], callback_data="SEARCHANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_11"] if Direct == True else _["ST_B_12"],
                callback_data="MODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_13"], callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_8"] if Group == True else _["ST_B_9"],
                callback_data="CHANNELMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_14"], callback_data="PLAYTYPEANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_8"] if Playtype == True else _["ST_B_9"],
                callback_data="PLAYTYPECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons
