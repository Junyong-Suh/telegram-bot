# telegram-bot

A simple Python script template to generate a Telegram bot to notify you whatever you want

## Requirements

* Requires Python 3.7.4+
* The only dependency: [requests](https://requests.readthedocs.io/en/master/)

## Quick Start

### Clone the Code

```
$ git clone git@github.com:Junyong-Suh/telegram-bot.git
```

### Install Dependencies

```
$ python --version
Python 3.7.7
$ cd telegram-bot
$ pip3 install -r requirements.txt
```

### Set Your Credentials

Rename `credentials_empty.py` to `credentials.py` and set your credentials

* How to get your own Telegram Bot and the ID: [https://core.telegram.org/bots](https://core.telegram.org/bots)

Add your Telegram ID(s) to `constants.py`

* How to get your Telegram ID: [https://support.bigone.com/hc/en-us/articles/360008014894-How-to-get-the-Telegram-user-ID-](https://support.bigone.com/hc/en-us/articles/360008014894-How-to-get-the-Telegram-user-ID-)

(Optional) Once you update your credentials, make Git not to track the file

```
# untrack
$ git update-index --assume-unchanged confidentials.py

# track again
# git update-index --no-assume-unchanged confidentials.py
```

### Subscribe to Your Bot

Turn on your Telegram App, find your bot and add.

### Run the Script

```
python main.py
```
You will get messages from the bot

## Docker

Assume that you set the credentials and subscribed to your bot. 

* Build the image

```
docker build -t telegram-bot:latest .
```

* Run 

```
docker run telegram-bot:latest
```

## References
* [https://core.telegram.org/bots/api#making-requests](https://core.telegram.org/bots/api#making-requests)
* [https://core.telegram.org/bots/api#message](https://core.telegram.org/bots/api#message)

## Contributions

Please make an issue and a PR :-)
