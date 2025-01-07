from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '8066476673:AAHMTIEzxjGyJCeUNr1VYbUw1nva2ItUZGY'
BOT_USERNAME: Final = '@dahua_techbot'

#commands
async def start_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! I am a tech bot dedicated for 'Dahua Technology'. ")

async def help_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am here to help you. Please type something so I can respond!")

async def custom_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")



#Responses
    
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'

    if 'how are you' in processed:
        return 'I am good!'

    if 'i love python' in processed:
        return 'Practice more and more...'

    if 'what is your name' in processed:
        return 'I am your friendly chatbot!'

    if 'tell me a joke' in processed:
        return 'Why don’t scientists trust atoms? Because they make up everything!'

    if 'what can you do' in processed:
        return 'I can chat with you, answer questions, and assist with your tasks!'

    if 'who created you' in processed:
        return 'I was created by a brilliant mind!'

    if 'what is python' in processed:
        return 'Python is a versatile programming language loved by developers.'

    if 'goodbye' in processed or 'bye' in processed:
        return 'Goodbye! Have a great day!'

    if 'thank you' in processed or 'thanks' in processed:
        return 'You’re welcome! Happy to help.'

    if 'what is the time' in processed:
        from datetime import datetime
        return f'The current time is {datetime.now().strftime("%H:%M:%S")}.'

    if 'recommend a book' in processed:
        return 'Sure! "Python Crash Course" by Eric Matthes is great for beginners.'

    if 'do you know bengali history' in processed:
        return 'Yes, Bengali history is rich and fascinating. Let me know what you’d like to learn!'

    
    return 'Sorry! I do not understand what you are talking about.'



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str =  update.message.chat.type
    text: str = update.message.text

    print(f'User {update.message.chat.id} in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('starting bot....')
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #errors
    app.add_error_handler(error)

    #polls the bot
    print('Polling....')
    app.run_polling(poll_interval=3)