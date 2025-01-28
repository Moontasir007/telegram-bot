import requests
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler, CallbackContext

# RAG API Configuration
API_URL = "https://payload.vextapp.com/hook/2Y5FMML2K0/catch/hello"
API_KEY = "or59R5MC.NLD3e4QtqcFpafuv4n2nV4GnyqjEeHDE"

async def start(update: Update, context: CallbackContext):
    """Handles the /start command"""
    await update.message.reply_text("Hello! Send me a message, and I'll process it through the RAG pipeline.")

async def handle_message(update: Update, context: CallbackContext):
    """Handles user messages and sends them to the RAG pipeline"""
    user_input = update.message.text
    
    headers = {
        "Content-Type": "application/json",
        "Apikey": f"Api-Key {API_KEY}"
    }
    
    payload = {
        "payload": user_input
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            api_output = response.json().get(response.text, "No response received.")
        else:
            api_output = f"Error: {response.status_code}, {response.text}"
    except Exception as e:
        api_output = f"API request failed: {str(e)}"
    
    await update.message.reply_text(api_output)

if __name__ == "__main__":
    bot = ApplicationBuilder().token("8066476673:AAHMTIEzxjGyJCeUNr1VYbUw1nva2ItUZGY").build()

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    bot.run_polling()