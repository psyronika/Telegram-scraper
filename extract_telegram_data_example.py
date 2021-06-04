from telethon import TelegramClient, events, sync
from telethon import functions, types
import pandas as pd
import sys
import os
from datetime import datetime

import telethon
print(telethon.__version__)

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
# https://my.telegram.org/apps

api_id = 5813010
api_hash = 'e83f29bc53a39155751b19dc510ec0e5'

def display_user_info(user):
    print(' - ', user.id, ',', user.last_name, ',', user.first_name, ' - ', user.username)
    #print(str(user))

# This script only works for public Telegram chats, which start with https://t.me.
# Source refers to a csv file with links to Telegram chats stored on my computer.

def process_source(_type, client, source, posts, output_folder):
    i=1
    print(_type + ' :', source)
    if str(source).startswith('https://t.me/'):
        source = source[0:]
    #if str(channel).startswith('https://t.me/joinchat'):
        #channel = channel[22:]
        #print(' Channel Modified:', channel)
        try:
            for user in client.iter_participants(source):
                new_row = pd.DataFrame({_type: [source], 'userid': [str(user.id)], 'username': [str(user.username)]})
                i=i+1
                posts = posts.append(new_row)
            posts.to_csv(output_folder + "\\telegram_" + _type + "_" + source + ".csv", index=False, header=True)
        except:
            print ('!!! Error for :', _type, sys.exc_info())

def process_sources(_type, client, sources, output_folder):
    posts = pd.DataFrame(columns=[_type, 'userid', 'username'])
    print('==============================')
    print(' Telegram ', _type)
    print('==============================')
    for source in sources:
        process_source(_type, client, source, posts, output_folder)

now = datetime.now() # current date and time
date_time = now.strftime("%Y.%m.%d_%H.%M.%S")
print("date and time:",date_time)
output_folder = 'results\\results_' + date_time
os.mkdir(output_folder)

client = TelegramClient('session_name', api_id, api_hash)
client.start()

'''
excel_source = pd.read_csv('sources\Telegram_channels.csv')
channels = excel_source['links'].tolist()
process_sources('channel', client, channels, output_folder)
'''

source = pd.read_csv('/Users/m.simonuva.nl/Documents/GitHub/Telegram-scraper/Telegram-scraper/Telegram_chats.csv')
chats = source['links'].tolist()
process_sources('chat', client, chats, output_folder)

'''
channels = pd.read_csv('/Users/m.simonuva.nl/Documents/GitHub/Telegram-scraper/Telegram-scraper/Telegram_channels', names=['1','2','channel'])
print(channels)
for i, row in channels.iterrows():
    c = row['channel']
    if str(c).startswith('https://t.me/'):
        print (c, c[13:])
    else:
        print ('!!! Skipping:' + str(c))

client = TelegramClient('session_name', api_id, api_hash)
client.start()
excel_channels = pd.read_csv('telegram_channels.csv')
channels = excel_channels['channel'].tolist()
display_channels(client, channels)
'''
