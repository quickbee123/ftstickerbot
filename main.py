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

    token = os.environ.get('TOKEN')
    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler(["start","help","h"],start))
    dispatcher.add_handler(InlineQueryHandler(inlinequery))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()    

