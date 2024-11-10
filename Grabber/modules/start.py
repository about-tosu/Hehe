import random
from html import escape 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler

from Grabber import application, PHOTO_URL, SUPPORT_CHAT, UPDATE_CHAT, BOT_USERNAME, db, GROUP_ID
from Grabber import pm_users as collection 


async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    username = update.effective_user.username

    user_data = await collection.find_one({"_id": user_id})

    if user_data is None:
        
        await collection.insert_one({"_id": user_id, "first_name": first_name, "username": username})
        
        await context.bot.send_message(chat_id=GROUP_ID, 
                                       text=f"New user Started The Bot..\n User: <a href='tg://user?id={user_id}'>{escape(first_name)})</a>", 
                                       parse_mode='HTML')
    else:
        
        if user_data['first_name'] != first_name or user_data['username'] != username:
            
            await collection.update_one({"_id": user_id}, {"$set": {"first_name": first_name, "username": username}})

    

    if update.effective_chat.type== "private":
        
        
        caption = f"""
               ***Hey there! {update.effective_user.first_name}***
              
**Hᴇʟʟᴏ, Wᴀɪғᴜ Sɴᴀᴛᴄʜᴇʀs! 
I ᴀᴍ ˹sɴᴀᴛᴄʜ ʏᴏᴜʀ ᴡᴀɪғᴜ˼
Wᴇʟᴄᴏᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴜʟᴛɪᴍᴀᴛᴇ ᴅᴇsᴛɪɴᴀᴛɪᴏɴ ғᴏʀ ғɪɴᴅɪɴɢ ʏᴏᴜʀ ᴘᴇʀғᴇᴄᴛ ᴡᴀɪғᴜ. 
Dɪᴠᴇ ɪɴ, ᴇxᴘʟᴏʀᴇ, ᴀɴᴅ ʟᴇᴛ ᴛʜᴇ ғᴜɴ ʙᴇɢɪɴ!

───────❪❂❫────────
➲ 𝗠𝘆 𝗝𝗼𝗯 - 𝚂𝚙𝚊𝚠𝚗𝚒𝚗𝚐 𝚆𝚊𝚒𝚏𝚞𝚜 𝚒𝚗 𝙶𝚛𝚘𝚞𝚙𝚜 𝚝𝚘 𝚂𝚗𝚊𝚝𝚌𝚑
➲ 𝗨𝘀𝗮𝗴𝗲 - 𝙹𝚞𝚜𝚝 𝙰𝚍𝚍 𝚖𝚎 𝚒𝚗 𝚢𝚘𝚞𝚛 𝙶𝚛𝚘𝚞𝚙. 𝙹𝚘𝚒𝚗 - @grabber_world 𝚏𝚘𝚛 𝚖𝚘𝚛𝚎 𝚚𝚞𝚎𝚛𝚒𝚎𝚜 
───────❪❂❫────────****
          """
        
        keyboard = [
            [InlineKeyboardButton("❀ ＡＤＤ ＭＥ ❀", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("ɢʀᴀʙʙᴇʀ ᴡᴏʀʟᴅ ➹", url=f'https://t.me/grabber_world'),
            InlineKeyboardButton("★UPDATES★", url=f'https://t.me/snatch_updates')],
            [InlineKeyboardButton("♤ ʜᴇʟᴘ ♤", callback_data='help')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        photo_url = random.choice(PHOTO_URL)

        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption,reply_markup=reply_markup )
    
    else:
        photo_url = random.choice(PHOTO_URL)
        keyboard = [
            [InlineKeyboardButton("❀ ＡＤＤ ＭＥ ❀", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("ɢʀᴀʙʙᴇʀ ᴡᴏʀʟᴅ ➹", url=f'https://t.me/grabber_world'),
            InlineKeyboardButton("★UPDATES★", url=f'https://t.me/snatch_updates')],
            [InlineKeyboardButton("♤ ʜᴇʟᴘ ♤", callback_data='help')]            
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption="🎴Alive!?... \n connect to me in PM For more information ",reply_markup=reply_markup )

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'help':
        help_text = """
    ***Help Section:***
    
***/snatch -To Guess waifu (only works in group)***
***/fav - Add Your fav***
***/trade - To trade waifu***
***/gift - Give any waifu to another user.. (only works in groups)***
***/harem - To see Your waifu***
***/topgroups - See Top Groups.. Ppl Guesses Most in that Groups***
***/top - Too See Top Users***
***/ctop - Your ChatTop***
***/changetime - Change waifu appear time (only works in Groups)***
***/explore - to get rewards***
***/daily -  reward increase too***
***/sell - <character id> for sell***
***/buy - for buy waifu***
***/marry - to marry a random waifu***
***/shop - waifu shop to buy waifu***
***/sbet - to bet tokenran***
***/propose - to propose random waifu***
***/claim - for daily rewards***
***/coin - to check current balance***
***/profile - to check your profile rank***
***/wsell - to sell any waifu and get some tokens***
***/xfight - fight dungenons and get tokens and other rewards***
***/rob - to robber any person tokens ( rob only who have low token )***
***/gamble - to bet the tokens with loss or profit***

     """
        help_keyboard = [[InlineKeyboardButton("⤾ Bᴀᴄᴋ", callback_data='back')]]
        reply_markup = InlineKeyboardMarkup(help_keyboard)
        
        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=help_text, reply_markup=reply_markup, parse_mode='markdown')

    elif query.data == 'back':

        caption = f"""
            **Hᴇʟʟᴏ, Wᴀɪғᴜ Sɴᴀᴛᴄʜᴇʀs! 
I ᴀᴍ ˹sɴᴀᴛᴄʜ ʏᴏᴜʀ ᴡᴀɪғᴜ˼
Wᴇʟᴄᴏᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴜʟᴛɪᴍᴀᴛᴇ ᴅᴇsᴛɪɴᴀᴛɪᴏɴ ғᴏʀ ғɪɴᴅɪɴɢ ʏᴏᴜʀ ᴘᴇʀғᴇᴄᴛ ᴡᴀɪғᴜ. 
Dɪᴠᴇ ɪɴ, ᴇxᴘʟᴏʀᴇ, ᴀɴᴅ ʟᴇᴛ ᴛʜᴇ ғᴜɴ ʙᴇɢɪɴ!
       """

        
        keyboard = [
            [InlineKeyboardButton("❀ ＡＤＤ ＭＥ ❀", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("ɢʀᴀʙʙᴇʀ ᴡᴏʀʟᴅ ➹", url=f'https://t.me/grabber_world'),
            InlineKeyboardButton("UPDATES", url=f'https://t.me/snatch_updates')],
            [InlineKeyboardButton("♤ ʜᴇʟᴘ ♤", callback_data='help')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=caption, reply_markup=reply_markup, parse_mode='markdown')


application.add_handler(CallbackQueryHandler(button, pattern='^help$|^back$', block=False))
start_handler = CommandHandler('start', start, block=False)
application.add_handler(start_handler)
