from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler
from Grabber import application, user_collection, collection
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Command to check waifu information
async def check(update, context):
    if len(context.args) != 1:
        await update.message.reply_text("Usage: /s <waifu_id>")
        return

    waifu_id = context.args[0]
    logger.info(f"Checking waifu information for ID: {waifu_id}")

    try:
        # Retrieve waifu information from the anime_characters collection based on the waifu ID
        waifu_info = await collection.find_one({'id': waifu_id})
        logger.info(f"Retrieved waifu information: {waifu_info}")

        if waifu_info:
            # Extract waifu details
            name = waifu_info.get('name', 'Unknown')
            anime = waifu_info.get('anime', 'Unknown')
            rarity = waifu_info.get('rarity', 'Unknown')
            picked_times = waifu_info.get('picked_times', 0)
            image_url = waifu_info.get('img_url', '')

            # Compose waifu information message
            message = f"𝐂𝐡𝐚𝐫𝐚𝐜𝐭𝐞𝐫 𝐝𝐞𝐭𝐚𝐢𝐥𝐬 ‼️\n\n" \
                      f"✨𝙽𝙰𝙼𝙴: {name}\n" \
                      f"⛩ᴀɴɪᴍᴇ: {anime}\n" \
                      f"𝚁𝙰𝚁𝙸𝚃𝚈: {rarity}\n\n" \
                      f"Globally picked {picked_times} Times..."

            # Send waifu information with the image
            if image_url:
                await update.message.reply_photo(photo=image_url, caption=message)
            else:
                await update.message.reply_text(message)
        else:
            await update.message.reply_text("Waifu information not found or invalid ID.")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        await update.message.reply_text(f"An error occurred: {e}")

# Add the command handler to your application
application.add_handler(CommandHandler("Lcheck", check))
            
