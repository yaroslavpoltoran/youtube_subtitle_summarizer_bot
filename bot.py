import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from backend import get_summary, translate_text

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_html("Hello! Send me a YouTube video link.")


async def send_subs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    video_url = update.message.text
    await update.message.reply_text("Please wait for a while...")

    summary = get_summary(video_url=video_url)

    if summary is None:
        await update.message.reply_text("Sorry, there is no summary :(")
    else:
        await update.message.reply_text(summary)

        translation = translate_text(text=summary, target_lang='ru')
        await update.message.reply_text(translation)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_subs))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
