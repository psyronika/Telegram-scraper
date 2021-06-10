#!/Users/m.simonuva.nl/opt/anaconda3/bin/python3

from telethon import TelegramClient
import asyncio
import argparse
from tqdm import tqdm
import time
import csv
import json


def get_keys(path):
    with open(path) as f:
        return json.load(f)

def read_links(filename):
    '''reads a newline-delimited text file with links and returns a list of links'''
    with open(filename) as f:
        links = [e.strip() for e in f.readlines() if len(e.strip())>0]
        return links


async def retrieve_single_chat(chat):
    '''takes link to a telegram chat as input and returns a list with its contents'''
    result = []
    await asyncio.sleep(60)
    async for msg in client.iter_messages(chat): 
        result.append([chat, msg.date, msg.sender_id, msg.id, msg.text])
    return result


def preprocess(row):
    ''' takes a row as returned from telethon and preprocesses it before saving'''
    try:
        row[1] = row[1].strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    except Exception as e:
        print(f"Could not preprocess the row {row}")
        print("Full error message:")
        print(e)
    return row


def retrieve_chats(listofchats):
    '''takes a list of links to telegram chat as input and returns a geneator that yields for each
    chat a lists with its contents'''
    for link in tqdm(listofchats):
        #return (preprocess(row) for row in client.loop.run_until_complete(retrieve_single_chat(link)))
        for row in client.loop.run_until_complete(retrieve_single_chat(link)):
            yield preprocess(row)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Tool to scrape info from telegram.')
    parser.add_argument('linkfile', type=str, help='a newline-delimited text file with Telegram links to scrape')
    parser.add_argument('outputfile',type=str, help='a name for the csv file to create')
    parser.add_argument('--noheader', action="store_true", help="don't write header to csv")
    args = parser.parse_args()

    keys = get_keys('/Users/m.simonuva.nl/Documents/secret/Telegram_keys.json')
    API_ID = keys['API_ID']
    API_HASH = keys['API_HASH']

    links = read_links(args.linkfile)
    print(f"Read {len(links)} links.")

    client = TelegramClient('session',API_ID, API_HASH)
    results = []
    with open(args.outputfile, mode='w') as f:
        writer = csv.writer(f)
        if not args.noheader:
            header = ['chat', 'date', 'sender_id', 'message_id', 'text']
            writer.writerow(header)
        with client:
            for chatdata in retrieve_chats(links):
                writer.writerow(chatdata)  


     


