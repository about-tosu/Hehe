import math
import asyncio
from datetime import datetime, timedelta
from telegram.ext import CommandHandler
from Grabber import application, user_collection
import math
import random
import time

async def balance(update, context):
    user_id = update.effective_user.id

    user_data = await user_collection.find_one({'id': user_id})

    if user_data:
        balance_amount = user_data.get('balance', 0)
        balance_message = f"𝙔𝙤𝙪𝙧 𝘾𝙪𝙧𝙧𝙚𝙣𝙩 𝘽𝙖𝙡𝙖𝙣𝙘𝙚 ⚖️ 𝙄𝙨:  $ {balance_amount} 𝙂𝙤𝙡𝙙 𝙘𝙤𝙞𝙣𝙨🪙!!"    
    else:
        balance_message = "𝙔𝙤𝙪 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙚𝙡𝙞𝙜𝙞𝙗𝙡𝙚 𝙏𝙤 𝙗𝙚 𝙖 𝙃𝙪𝙣𝙩𝙚𝙧⚔️"

    await update.message.reply_text(balance_message)

application.add_handler(CommandHandler("gold", balance, block=False))
