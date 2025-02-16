from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import random

# Replace with your bot token
TOKEN = "7363659568:AAETJw36lqVKVqDX1WRCJ1a3_aKOT6PY5U0"

# Function to start the bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Welcome! Type /game to start the minigame.")

# Function to start the game
async def game(update: Update, context: CallbackContext) -> None:
    number = random.randint(1, 10)
    context.user_data['number'] = number
    await update.message.reply_text("I have picked a number between 1 and 10. Try to guess it!")

# Function to handle guesses
async def guess(update: Update, context: CallbackContext) -> None:
    if 'number' not in context.user_data:
        await update.message.reply_text("Start the game first by typing /game!")
        return

    try:
        user_guess = int(update.message.text)
        correct_number = context.user_data['number']

        if user_guess == correct_number:
            await update.message.reply_text("🎉 Correct! You won! Type /game to play again.")
            del context.user_data['number']  # Reset game
        else:
            await update.message.reply_text("❌ Wrong! Try again.")

    except ValueError:
        await update.message.reply_text("Please enter a valid number!")

# Main function to run the bot
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("game", game))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, guess))

    app.run_polling()

if __name__ == '__main__':
    main()
