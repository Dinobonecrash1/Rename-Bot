from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """
𝐁𝐮𝐲   𝐏𝐥𝐚𝐧   𝐀𝐜𝐜.   𝐓𝐨   𝐘𝐨𝐮𝐫   𝐍𝐞𝐞𝐝 !!!


𝟏.   𝐅𝐫𝐞𝐞 𝐏𝐥𝐚𝐧

👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ 2 ɢʙ
👉     ꜰʀᴇᴇ


𝟐.   𝐁𝐚𝐬𝐢𝐜  𝐏𝐥𝐚𝐧

👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  10 ɢʙ
👉     ʙᴜʏ  <a href='https://telegra.ph/Rename-Bot-premium-09-29'>₹ 30/ᴍᴏɴᴛʜ.</a> 
	

𝟑.   𝐒𝐭𝐚𝐧𝐝𝐚𝐫𝐝  𝐏𝐥𝐚𝐧 

👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  50 ɢʙ
👉     ʙᴜʏ  <a href='https://telegra.ph/Rename-Bot-premium-09-29'>₹ 70/ᴍᴏɴᴛʜ.</a>  
	

𝟒.   𝐏𝐫𝐞𝐦𝐢𝐮𝐦  𝐏𝐥𝐚𝐧 

👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  100 ɢʙ
👉     ʙᴜʏ  <a href='https://telegra.ph/Rename-Bot-premium-09-29'>₹ 150/ᴍᴏɴᴛʜ.</a>

•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•

𝐍𝐎𝐓𝐄 :  ᴀꜰᴛᴇʀ  ᴘᴀʏᴍᴇɴᴛ  ꜱᴇɴᴅ  ꜱᴄʀᴇᴇɴꜱʜᴏᴛ  ᴛᴏ  ᴏᴡɴᴇʀ.
"""
	keybord = InlineKeyboardMarkup(
                [
                    [
            InlineKeyboardButton('ᴄᴏɴᴛᴀᴄᴛ  ᴛᴏ  ᴏᴡɴᴇʀ  ❣️',url='https://telegram.me/Zenitsu_AF')
            ],
                    [
            InlineKeyboardButton('ʙᴜʏ   ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ   😊',url='https://telegra.ph/Rename-Bot-premium-09-29')
            ],
                    [
                        InlineKeyboardButton('🔮  ʜᴇʟᴘ',url='https://t.me/Kdrama_Clan'),
                        InlineKeyboardButton("🏠   ʜᴏᴍᴇ", callback_data = "cancel")
                    ]
                ]
            )
	await update.message.edit(text = text, disable_web_page_preview=True, reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """
𝐁𝐮𝐲   𝐏𝐥𝐚𝐧   𝐀𝐜𝐜.   𝐓𝐨   𝐘𝐨𝐮𝐫   𝐍𝐞𝐞𝐝 !!!


𝟏.   𝐅𝐫𝐞𝐞 𝐏𝐥𝐚𝐧

👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ 2 ɢʙ
👉     ꜰʀᴇᴇ


𝟐.   𝐁𝐚𝐬𝐢𝐜  𝐏𝐥𝐚𝐧

👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  10 ɢʙ
👉     ʙᴜʏ  <a href='https://telegra.ph/Rename-Bot-premium-09-29'>₹ 30/ᴍᴏɴᴛʜ.</a> 
	

𝟑.   𝐒𝐭𝐚𝐧𝐝𝐚𝐫𝐝  𝐏𝐥𝐚𝐧 

👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  50 ɢʙ
👉     ʙᴜʏ  <a href='https://telegra.ph/Rename-Bot-premium-09-29'>₹ 70/ᴍᴏɴᴛʜ.</a>  
	

𝟒.   𝐏𝐫𝐞𝐦𝐢𝐮𝐦  𝐏𝐥𝐚𝐧 

👉     ᴅᴀɪʟʏ  ʟɪᴍɪᴛ  100 ɢʙ
👉     ʙᴜʏ  <a href='https://telegra.ph/Rename-Bot-premium-09-29'>₹ 150/ᴍᴏɴᴛʜ.</a>

•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•

𝐍𝐎𝐓𝐄 :  ᴀꜰᴛᴇʀ  ᴘᴀʏᴍᴇɴᴛ  ꜱᴇɴᴅ  ꜱᴄʀᴇᴇɴꜱʜᴏᴛ  ᴛᴏ  ᴏᴡɴᴇʀ.
"""
	keybord = InlineKeyboardMarkup(
                [
                    [
            InlineKeyboardButton('ᴄᴏɴᴛᴀᴄᴛ  ᴛᴏ  ᴏᴡɴᴇʀ  ❣️',url='https://telegram.me/Zenitsu_AF')
            ],
                    [
            InlineKeyboardButton('ʙᴜʏ   ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ   😊',url='https://telegra.ph/Rename-Bot-premium-09-29')
            ],
                    [
                        InlineKeyboardButton('🔮  ʜᴇʟᴘ',url='https://t.me/Kdrama_Clan'),
                        InlineKeyboardButton("🏠   ʜᴏᴍᴇ", callback_data = "cancel")
                    ]
                ]
            )
	await message.reply_text(text = text, disable_web_page_preview=True, reply_markup = keybord)
