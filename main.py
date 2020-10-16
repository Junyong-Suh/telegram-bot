import config
import time
import logging
import sys
import constants as c
from lib import notification as notify, target_service


# the very main entry
def main(argv, is_local=True):
    # exit if no receiver
    if not config.TELEGRAM_IDS_SUBSCRIBER:
        logging.error("No Telegram IDs to notify")
        return

    while True:
        # get the current application counts
        your_alarm = target_service.call_your_api()
        if your_alarm is c.EMPTY_RESPONSE:
            continue  # api failure

        # log
        logging.info(your_alarm)

        # and notify via Telegram
        notify.to_subscribers(your_alarm)

        # check every day
        time.sleep(c.DAY_IN_SECONDS)


# main
if __name__ == "__main__":
    if 1 < len(sys.argv) and sys.argv[1] == "production":
        logging.basicConfig(level=logging.INFO)
        main(sys.argv[2:], False)  # prod
    else:
        logging.basicConfig(level=logging.DEBUG)
        main(sys.argv[2:], True)   # local
