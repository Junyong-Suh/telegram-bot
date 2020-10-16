import config
from lib import telegram


# notify to all subscribers
def to_subscribers(msg):
    telegram.notify_on_telegram(config.TELEGRAM_IDS_SUBSCRIBER, msg)
