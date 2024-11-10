from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
import random
from datetime import datetime, timedelta
from Grabber import application, user_collection

# Dictionary to store user's last shunt time
last_shunt_time = {}

# Command handler for /sbag

async def toss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_data = await user_collection.find_one({'id': user_id})
    user_balance = user_data.get('balance', 0)

    # Check if the user provided arguments
    if not context.args or len(context.args) != 2:
        await update.message.reply_text("Usage: /toss [amount] [H/T]")
        return

    try:
        amount = int(context.args[0])
        choice = context.args[1].upper()
    except ValueError:
        await update.message.reply_text("Invalid amount. Please enter a number.")
        return

    if choice not in ['H', 'T']:
        await update.message.reply_text("Invalid choice. Please choose H for heads or T for tails.")
        return

    if amount <= 0:
        await update.message.reply_text("Amount must be greater than 0.")
        return

    min_bet = user_balance * 0.07  # 7% of balance

    if amount < min_bet:
        await update.message.reply_text(f"You can't bet less than 7% of your balance, which is (${min_bet:.2f}).")
        return

    if user_balance < amount:
        await update.message.reply_text(f"You don't have enough balance! Your current balance is ${user_balance:,.0f}.")
        return

    # Coin landing randomly on head or tail
    coin_landing = random.choice(["H", "T"])

    if choice == coin_landing:
        won_amount = 2 * amount
        await user_collection.update_one({'id': user_id}, {'$inc': {'balance': won_amount - amount}})
        message = f"You chose {'Head' if choice == 'H' else 'Tail'} and won ${won_amount:,.0f}.\nCoin landed on {coin_landing}."
    else:
        await user_collection.update_one({'id': user_id}, {'$inc': {'balance': -amount}})
        message = f"You chose {'Head' if choice == 'H' else 'Tail'} and lost ${amount:,.0f}.\nCoin landed on {coin_landing}."

    await update.message.reply_text(message)
    await update.message.reply_photo(
        photo='https://telegra.ph/file/5fd5467de6e016a0dc38d-c9c8649ddd935df2e5.mp4',
        caption="Here is the coin toss result."
    )

# Register commands
application.add_handler(CommandHandler("toss", toss))
