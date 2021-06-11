import logging
import os
from dotenv import load_dotenv


from telegram.ext import Updater, CommandHandler, InlineQueryHandler

from actions.start import start
from actions.inlinequery import inlinequery

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main():

    TOKEN = os.getenv('TOKEN')
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler(["start","help","h"],start))
    dispatcher.add_handler(InlineQueryHandler(inlinequery))


    updater.start_webhook(listen="0.0.0.0", port=os.getenv('PORT', default=8000), url_path=TOKEN, webhook_url="https://ftstickerbot.herokuapp.com/"+TOKEN)

    updater.idle()

if __name__ == '__main__':
    main()    

