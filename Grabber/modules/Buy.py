from telegram.ext import CommandHandler
from Grabber import collection, user_collection, application
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram import InputMediaPhoto

async def buy(update, context):
    user_id = update.effective_user.id

    # Check if the command includes a character ID
    if not context.args or len(context.args) != 1:
        await update.message.reply_text('<b>Please provide a valid guess ID to buy.</b>')
        return

    character_id = context.args[0]

    # Retrieve the character from the store based on the provided ID
    character = await collection.find_one({'id': character_id})
    if not character:
        await update.message.reply_text('guess not found in the store.')
        return

    # Check if the user has sufficient coins to make the purchase
    user = await user_collection.find_one({'id': user_id})
    if not user or 'balance' not in user:
        await update.message.reply_text('Error: User balance not found.')
        return

    # Determine the coin cost based on the rarity of the character
    rarity_coin_mapping = {
        "🟢 𝘾𝙤𝙢𝙢𝙤𝙣": 4000,
        "🔵 𝙈𝙚𝙙𝙞𝙪𝙢": 8000,
        "🟡 𝙍𝙖𝙧𝙚": 15000,
        "🔴 𝙇𝙚𝙜𝙚𝙣𝙙𝙖𝙧𝙮": 30000,
        "🪽 𝙇𝙚𝙜𝙚𝙣𝙙𝙖𝙧𝙮": 30000,
        "🔮 𝙇𝙞𝙢𝙞𝙩𝙚𝙙": 60000,
        "❄ 𝙬𝙞𝙣𝙩𝙚𝙧": 100000,
    }

    rarity = character.get('rarity', 'Unknown Rarity')
    coin_cost = rarity_coin_mapping.get(rarity, 0)

    if coin_cost == 0:
        await update.message.reply_text('Invalid rarity. Cannot determine the coin cost.')
        return

    if user['balance'] < coin_cost:
        await update.message.reply_text('Insufficient coins to buy')
        return

    # Add the purchased character to the user's harem
    await user_collection.update_one(
        {'id': user_id},
        {'$push': {'characters': character}, '$inc': {'balance': -coin_cost}}
    )

    # Get the character's image URL from the database
    character_img_url = character.get('image_url', '')

    # Send the success message with the character's image attached
    await update.message.reply_text(
        f'Success! You have purchased {character["name"]} for {coin_cost} coins.'
    )

buy_handler = CommandHandler("buy", buy, block=False)
application.add_handler(buy_handler)

async def shop(update, context):
    # You can customize the message text based on your needs
    message_text = "♠︎𝙒𝙖𝙞𝙛𝙪 𝙨𝙝𝙤𝙥 𝙏𝙤 𝘽𝙪𝙮 𝘾𝙝𝙖𝙧𝙖𝙘𝙩𝙚𝙧𝙨 ♠︎\n\n"
    message_text += "🟢 𝘾𝙤𝙢𝙢𝙤𝙣: $ 4,000 💸\n"
    message_text += "🔵 𝙈𝙚𝙙𝙞𝙪𝙢: $ 8,000 💸\n"
    message_text += "🟡 𝙍𝙖𝙧𝙚:  $ 15,000 💸\n"
    message_text += "🔴 𝙇𝙚𝙜𝙚𝙣𝙙𝙖𝙧𝙮: $ 30,000 💸\n"
    message_text += "🪽 𝙇𝙚𝙜𝙚𝙣𝙙𝙖𝙧𝙮: $ 30,000 💸\n"
    message_text += "/buy <pick_id>"
    await update.message.reply_text(message_text)

# Register the new /shop command handler
shop_handler = CommandHandler("shop", shop, block=False)
application.add_handler(shop_handler)
