# Free Ton Sticker Bot

Free Ton Sticker Bot is a telegram bot which gives a set of stickers based on Free Ton on an inline request.

- Check out the bot at [@ftstickerbot](https://t.me/ftstickerbot)


## Installation and Deployment


### Installation

1. Clone the source code 
2. Install all requirements using the following command
   ```
   $ pip3 install -r requirements.txt
   ```

### Environment variables

Add environment variables

| Variable     | Description                         |
| --------     | -----------                         |
| TOKEN        | Token of bot generated by Botfather |
| DATABASE_URL | URL of database                     |
| DEV_ID       | Telegram ID of develope             |
| PORT         | The port to listen for webhooks     |
| URL          | The base URL for webhooks           |
| LISTEN       | The URL to listen for webhooks      |

### Deployment

Start the bot using the following command
```
$ python3 main.py 
```