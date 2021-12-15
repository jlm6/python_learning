from stock_function import *
import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

API_KEY = your_key
token = your_token

updater = Updater ( token )

logging.basicConfig (
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO
)

logger = logging.getLogger ( __name__ )


def start( update: Update, context: CallbackContext ) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2 (
        fr'Hi {user.mention_markdown_v2 ()} \!, this is a stock&crypto price tracker bot',
        reply_markup = ForceReply ( selective = True ),
    )

def echo( update: Update, context: CallbackContext ) -> None:
    """Echo the user message."""
    crypto = ['BTC', 'ETH', 'XRP', 'BCH', 'ADA', 'LTC', 'XEM', 'XLM', 'EOS', 'NEO', 'MIOTA', 'DASH', 'XMR', 'TRX',
              'XTZ', 'DOGE', 'ETC', 'VEN', 'USDT', 'BNB']
    update.message.reply_text ( "Please wait..." )
    if (update.message.text.isnumeric()):
        namestock = update.message.text
        update.message.reply_text (hkstock(namestock))
    elif update.message.text.upper() in crypto:
        update.message.reply_text(crypto_intraday(update.message.text, API_KEY))
    else:
        update.message.reply_text((new_daily(update.message.text, API_KEY)))

updater.dispatcher.add_handler ( MessageHandler ( Filters.text & ~Filters.command, echo ) )
updater.start_polling ()
updater.idle ()
