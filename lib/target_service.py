import requests
import logging
import constants as c


def call_your_api(timeout=3):
    try:
        r = requests.get(
            "API_TO_CALL",
            timeout=timeout
        )
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as e:
        logging.error(str(e))
    except requests.exceptions.ConnectionError as e:
        logging.error(str(e))
    except requests.exceptions.Timeout as e:
        logging.error(str(e))
    except requests.exceptions.RequestException as e:
        logging.error(str(e))
    return c.EMPTY_RESPONSE
