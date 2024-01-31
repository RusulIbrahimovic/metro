from typing import final, Final
import telegram.ext.filters as filters
from telegram import Update
from telegram.ext import Application,CommandHandler, MessageHandler,ContextTypes
TOKEN: final='6922135464:AAGhQGcgMslJzPE3cWXy9qKFiQZEfZtZMgc'
BOT_USERNAME: Final ='@MetroUOITC_bot'

#الاوامر اللي نحطها
async def start_command(update:Update, context: ContextTypes. DEFAULT_TYPE) :
    await update.message.reaply_text('Tracking your tasks performance')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
    Available commands:
    - /start: Starts the task tracking process.
    - /help: Displays this help message.

    To use the task tracking features, type /start.
    """
    await update.message.reply_text(help_text)

#اللوجيك هنا ونرجهعه ك نص
def handle_response(text: str) -> str:
    # TODO: Implement the actual response handling logic here
    # For now, it just returns a placeholder response
    return "Placeholder response"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type  # Get message type
    text = update.message.text  # Get message text

    print(f'User ({update.message.chat.id}) in ({message_type}): "{text}"')  # Print message log

    if message_type == 'group':  # Check if message is in a group chat
        if BOT_USERNAME in text:  # Check if bot is mentioned
            new_text = text.replace(BOT_USERNAME, '').strip()  # Remove bot mention
            response = handle_response(new_text)  # Call handle_response with modified text
        else:
            return  # Ignore messages without bot mention
    else:  # Handle private messages directly
        response = handle_response(text)  # Call handle_response with original text

    print('Bot: ', response)  # Print bot's response
    await update.message.reply_text(response)  # Send the response back to the user

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles errors that occur during message processing."""
    print(f"Update {update} caused error {context.error}")

if __name__ == '__main__':
    print('start')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Message handler (optional)
    app.add_handler (MessageHandler (filters.TEXT, handle_message))

    # Error handler
    app.add_error_handler(error)
    print('polling')
    app.run_polling(poll_interval=3)