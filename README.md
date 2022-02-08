# Telegram-scraper

This repository contains a python script to scrape Telegram chats/channels using a list of access words.
The code is largely based on the Telethon library: https://github.com/LonamiWebs/Telethon

## Requirements:

* api_keys: users must request Telegram API credentials (API ID and API HASH) by creating a Telegram application via https://core.telegram.org/#getting-started, creendtials can be entered directly when running the script or can be stored in json files
* linkfile: a new line delimited text file that contains links to the desired public Telegram chats or channels users wish to scrape
* outputfile: an empty csv files that stores results 
