from uuid import uuid4
from telegram import InlineQueryResultCachedSticker


def inlinequery(update, context):
    
    results = [
        InlineQueryResultCachedSticker(
            id=str(uuid4()),
            sticker_file_id="CAACAgQAAxkBAAECZnJgvxrdHErlU7x3Sb2bu1f35pnx6QACOQoAAvhy2VJRecsTuWsiBh8E"
            
        ),
        InlineQueryResultCachedSticker(
            id=str(uuid4()),
            sticker_file_id="CAACAgQAAxkBAAECZnJgvxrdHErlU7x3Sb2bu1f35pnx6QACOQoAAvhy2VJRecsTuWsiBh8E"
            
        ),
        InlineQueryResultCachedSticker(
            id=str(uuid4()),
            sticker_file_id="CAACAgQAAxkBAAECZnJgvxrdHErlU7x3Sb2bu1f35pnx6QACOQoAAvhy2VJRecsTuWsiBh8E"
            
        ),
        InlineQueryResultCachedSticker(
            id=str(uuid4()),
            sticker_file_id="CAACAgQAAxkBAAECZnJgvxrdHErlU7x3Sb2bu1f35pnx6QACOQoAAvhy2VJRecsTuWsiBh8E"
            
        ),
        InlineQueryResultCachedSticker(
            id=str(uuid4()),
            sticker_file_id="CAACAgQAAxkBAAECZnJgvxrdHErlU7x3Sb2bu1f35pnx6QACOQoAAvhy2VJRecsTuWsiBh8E"
            
        ),
        InlineQueryResultCachedSticker(
            id=str(uuid4()),
            sticker_file_id="CAACAgQAAxkBAAECZnJgvxrdHErlU7x3Sb2bu1f35pnx6QACOQoAAvhy2VJRecsTuWsiBh8E"
            
        )]
    update.inline_query.answer(results)    