from typing import Final
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '8066476673:AAHMTIEzxjGyJCeUNr1VYbUw1nva2ItUZGY'
BOT_USERNAME: Final = '@dahua_techbot'

# Define the Inline Keyboard Menus
MAIN_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("About", callback_data='about'),
     InlineKeyboardButton("Services", callback_data='services')],
    [InlineKeyboardButton("Help", callback_data='help'),
     InlineKeyboardButton("Contact", callback_data='contact')]
])

ABOUT_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("Our Mission", callback_data='about_mission')],
    [InlineKeyboardButton("Our History", callback_data='about_history')],
    [InlineKeyboardButton("Back to Main Menu", callback_data='main')]
])

SERVICES_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("Technical Support", callback_data='services_support')],
    [InlineKeyboardButton("Chatbot Assistance", callback_data='services_chatbot')],
    [InlineKeyboardButton("Back to Main Menu", callback_data='main')]
])

HELP_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("FAQs", callback_data='help_faqs')],
    [InlineKeyboardButton("User Guide", callback_data='help_guide')],
    [InlineKeyboardButton("Back to Main Menu", callback_data='main')]
])

CONTACT_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("Email Us", callback_data='contact_email')],
    [InlineKeyboardButton("Visit Website", callback_data='contact_website')],
    [InlineKeyboardButton("Back to Main Menu", callback_data='main')]
])

# Handle free-text responses
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

    return 'Sorry, I do not understand that. Can you try something else?'

# Command Handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command."""
    await update.message.reply_text("Welcome! Choose an option below:", reply_markup=MAIN_MENU)

# Callback Query Handler for inline keyboard
async def menu_navigation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button presses for the inline keyboard."""
    query = update.callback_query
    await query.answer()  # Acknowledge the callback query

    # Navigate based on the callback data
    if query.data == 'about':
        await query.edit_message_text("Learn more about us:", reply_markup=ABOUT_MENU)
    elif query.data == 'services':
        await query.edit_message_text("Explore our services:", reply_markup=SERVICES_MENU)
    elif query.data == 'help':
        await query.edit_message_text("How can we assist you?", reply_markup=HELP_MENU)
    elif query.data == 'contact':
        await query.edit_message_text("Get in touch with us:", reply_markup=CONTACT_MENU)
    elif query.data == 'about_mission':
        await query.edit_message_text("Our mission is to provide exceptional service and value to our users.", reply_markup=ABOUT_MENU)
    elif query.data == 'about_history':
        await query.edit_message_text("Our history dates back to our founding, where innovation began!", reply_markup=ABOUT_MENU)
    elif query.data == 'services_support':
        await query.edit_message_text("We offer 24/7 technical support to resolve your issues.", reply_markup=SERVICES_MENU)
    elif query.data == 'services_chatbot':
        await query.edit_message_text("Our chatbot assistance helps with quick solutions.", reply_markup=SERVICES_MENU)
    elif query.data == 'help_faqs':
        await query.edit_message_text("Here are some frequently asked questions to assist you.", reply_markup=HELP_MENU)
    elif query.data == 'help_guide':
        await query.edit_message_text("Check out our user guide for detailed instructions.", reply_markup=HELP_MENU)
    elif query.data == 'contact_email':
        await query.edit_message_text("You can email us at support@dahua.tech.", reply_markup=CONTACT_MENU)
    elif query.data == 'contact_website':
        await query.edit_message_text("Visit our website at https://www.dahua.tech for more information.", reply_markup=CONTACT_MENU)
    elif query.data == 'main':
        await query.edit_message_text("Welcome! Choose an option below:", reply_markup=MAIN_MENU)

# Message Handler for free-text input
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = handle_response(user_input)
    await update.message.reply_text(response)

# Error Handler
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors caused by updates."""
    print(f"Update {update} caused error {context.error}")

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Add Command and Callback Handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CallbackQueryHandler(menu_navigation))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Add Error Handler
    app.add_error_handler(error_handler)

    # Polling
    print('Polling...')
    app.run_polling(poll_interval=3)
