class Scripted(object):    


    PROGRESS_DIS = """\n
<b>📁 : {1} | {2}</b>\n
<b>🚀 : {0}%</b>\n
<b>⚡ : {3}/s</b>\n
<b>⏱️ : {4}</b>\n"""


    HELP_TEXT = """
<i>𝐖𝐚𝐭𝐜𝐡 𝐕𝐢𝐝𝐞𝐨 𝐇𝐨𝐰 𝐭𝐨 𝐔𝐬𝐞 𝐌𝐞 <a href='https://youtu.be/HnXdu74o34E'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></i>\n
<i>𝐒𝐞𝐧𝐝 𝐚 𝐩𝐡𝐨𝐭𝐨 𝐭𝐨 𝐦𝐚𝐤𝐞 𝐢𝐭 𝐚𝐬 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 (optional)</i>\n
<i>𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚𝐧𝐲 𝐟𝐢𝐥𝐞 (or) 𝐌𝐞𝐝𝐢𝐚 𝐟𝐫𝐨𝐦 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦</i>\n
<i>𝐂𝐨𝐧𝐯𝐞𝐫𝐭 𝐟𝐢𝐥𝐞𝐬 𝐢𝐧𝐭𝐨 𝐯𝐢𝐝𝐞𝐨 𝐮𝐬𝐞 /convert 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>\n
<i>𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐭𝐡𝐚𝐭 𝐟𝐢𝐥𝐞 𝐰𝐢𝐭𝐡 /rename 𝐧𝐞𝐰 𝐧𝐚𝐦𝐞.ext</i>\n
<i>𝐕𝐢𝐞𝐰 𝐲𝐨𝐮𝐫 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐝𝐨 /sthumbnail 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>\n
<i>𝐃𝐞𝐥𝐞𝐭𝐞 𝐲𝐨𝐮𝐫 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐝𝐨 /dthumbnail 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>"""


    ABOUT_TEXT = """
<b>🤖 𝐌𝐲 𝐍𝐚𝐦𝐞 : <a href='http://t.me/SL_Jana_Rename_Bot'>SL_Jana_Rename_Bot</a></b>\n
<b>📢 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : <a href='https://t.me/SL_Jana_Team'>SL_Jana_Team</a></b>\n
<b>👥 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 𝐕𝟐 : <a href='http://t.me/SL_Jana_Rename_Bot'>0.9.2 beta</a></b>\n
<b>📥 𝐒𝐨𝐮𝐫𝐜𝐞 : <a href='https://github.com/SLJaNa/Renamer-Bot'>Click Here</a></b>\n
<b>🌐 𝐒𝐞𝐫𝐯𝐞𝐫 : <a href='https://heroku.com'>Heroku</a></b>\n
<b>📕 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : <a href='https://t.me/SL_Jana_Team'>SL_Jana_Team</a></b>\n
<b>㊙ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞  : <a href='https://www.python.org'>Python 3.9.4</a></b>\n
<b>👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 : <a href='https://t.me/SL_Jana_Team'>꧁ SL_Jana_Team ꧂</a></b>\n
<b>📌 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : <a href='https://t.me/SL_Jana_Team'>꧁ SL_Jana_Team ꧂</a></b>\n"""


    CUSTOM_CAPTION = "<i>{}</i>"
    ACCESS_DENIED = "<b>¥ou 𝐀𝐫𝐞 𝐁𝐚𝐧𝐧𝐞𝐝 🚫</b>"
    BANNED_USER_TEXT = "<i>¥ou 𝐀𝐫𝐞 𝐁𝐚𝐧𝐧𝐞𝐝 🚫</i>"
    TRYING_TO_UPLOAD = "<i>𝐓𝐫𝐲𝐢𝐧𝐠 𝐭𝐨 𝐮𝐩𝐥𝐨𝐚𝐝....</i>"
    CURRENT_THUMBNAIL = "<i>𝐘𝐨𝐮𝐫 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 🎭</i>"
    THUMBNAIL_SAVED = "<i>𝐘𝐨𝐮𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐒𝐚𝐯𝐞𝐝 ✅</i>"
    THUMBNAIL_DELETED = "<i>𝐘𝐨𝐮𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 ✅</i>"
    NO_THUMBNAIL_FOUND = "<i>𝐍𝐨 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐅𝐨𝐮𝐧𝐝 😔</i>"
    TRYING_TO_DOWNLOAD = "<i>𝐓𝐫𝐲𝐢𝐧𝐠 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝....</i>"
    UPLOAD_SUCCESS = "<u><i>❣️𝓣𝓱𝓪𝓷𝓴𝓼 𝓕𝓸𝓻 𝓤𝓼𝓲𝓷𝓰 𝓜𝓮❣️@SL_Jana_Rename_Bot</i></u>"
    REPLY_TO_MEDIA = "<i>𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐭𝐡𝐚𝐭 𝐌𝐞𝐝𝐢𝐚 𝐰𝐢𝐭𝐡 /convert</i>"
    UPLOAD_START = "<i>📤 𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐲𝐨𝐮𝐫 𝐟𝐢𝐥𝐞 𝐩𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭...</i>\n"
    DOWNLOAD_START = "<i>📥 𝐃𝐨𝐰𝐧𝐥𝐨𝐝𝐢𝐧𝐠 𝐲𝐨𝐮𝐫 𝐟𝐢𝐥𝐞 𝐩𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭...</i>\n"
    JOIN_NOW_TEXT = "<code>💢𝔽𝕚𝕣𝕤𝕥 𝕁𝕠𝕚𝕟 𝕄𝕪 𝕌𝕡𝕕𝕒𝕥𝕖𝕤 ℂ𝕙𝕒𝕟𝕟𝕖𝕝 𝕋𝕠 𝕌𝕤𝕖 𝕄𝕖💢@SL_Jana_Team</code>"
    REPLY_TO_FILE = "<i>𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐭𝐡𝐚𝐭 𝐟𝐢𝐥𝐞 𝐰𝐢𝐭𝐡 /rename 𝐧𝐞𝐰 𝐧𝐚𝐦𝐞 .𝐞𝐱𝐭</i>"
    CONTACT_MY_DEVELOPER = "<i>❗❗𝓢𝓸𝓶𝓽𝓱𝓲𝓷𝓰 𝓦𝓻𝓸𝓷𝓰.𝓒𝓸𝓷𝓽𝓪𝓬𝓽 𝓜𝔂 𝓓𝓮𝓿𝓮𝓵𝓸𝓹𝓮𝓻❗❗🤯@SL_Jana_Team</i>"
    START_TEXT = "<i>🤖𝓣𝓱𝓲𝓼 𝓲𝓼 𝓪 𝓢𝓲𝓶𝓹𝓵𝓮 𝓕𝓲𝓵𝓮 𝓡𝓮𝓷𝓪𝓶𝓮𝓻 & 𝓕𝓲𝓵𝓮 𝓒𝓸𝓷𝓿𝓮𝓻𝓽𝓮𝓻 𝓑𝓸𝓽 𝔀𝓲𝓽𝓱 𝓹𝓮𝓻𝓶𝓪𝓷𝓮𝓷𝓽 𝓽𝓱𝓾𝓶𝓫𝓷𝓪𝓲𝓵 𝓼𝓾𝓹𝓹𝓸𝓻𝓽🤖💯@𝕊𝕃_𝕁𝕒𝕟𝕒_ℝ𝕖𝕟𝕒𝕞𝕖_𝔹𝕠𝕥</i>"
    UPGRADE_TEXT = "<b>a⬆️𝐓𝐨 𝐮𝐩𝐠𝐫𝐚𝐝𝐞 𝐲𝐨𝐮𝐫 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧⬆️<a href='https://t.me/SL_Jana_Team'>SL_Jana_Team</a></b>"
