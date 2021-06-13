from telegram.ext import CommandHandler, InlineQueryHandler, ConversationHandler, Filters, MessageHandler

from actions.start import start
from actions.inlinequery import inlinequery
from actions.insert_sticker import add_sticker,get_sticker_id,cancel


handlers = {
    CommandHandler: [
        ({"command":["start","help","h"],"callback":start},)
    ],
    InlineQueryHandler: [
        ({"callback":inlinequery},)
    ],
    ConversationHandler: [
        ({
            "entry_points":[CommandHandler('addsticker',add_sticker)],
            "states":{
                1 : [MessageHandler(Filters.text & ~Filters.command,get_sticker_id)]
            },
            "fallbacks": [CommandHandler('cancel',cancel)]
        },)
    ]
}