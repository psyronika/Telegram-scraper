#!/Users/m.simonuva.nl/opt/anaconda3/bin/python3

from telethon import TelegramClient
import asyncio
import argparse
from tqdm import tqdm
import time
import csv


API_ID = 5813010
API_HASH = 'e83f29bc53a39155751b19dc510ec0e5'



def read_links(filename):
    '''reads a newline-delimited text file with links and returns a list of links'''
    with open(filename) as f:
        links = [e.strip() for e in f.readlines() if len(e.strip())>0]
        return links


async def connect(api_id, api_hash):
    try:
        await client.start()
        await client.connect()
    except OSError:
        print('Failed to connect')


async def sayhi():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Hello to myself!')

async def getresults(chat):
    result = []
    await asyncio.sleep(1)
    async for msg in client.iter_messages(chat): 
        result.append([msg.date, msg.sender_id, msg.id, msg.text])
    return result


def preprocess(row):
    ''' takes a row as returned from telethon and preprocesses it before saving'''
    row[0] = row[0].strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return row

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Tool to scrape info from telegram.')
    parser.add_argument('linkfile', type=str, help='a newline-delimited text file with Telegram links to scrape')
    parser.add_argument('outputfile',type=str, help='a name for the csv file to create')
    parser.add_argument('--noheader', action="store_true", help="don't write header to csv")
    args = parser.parse_args()

    links = read_links(args.linkfile)
    print(f"Read {len(links)} links.")

    # TODO: consider outsourcing this to a function 


    #asyncio.run(main())
    # asyncio.run(connect(API_ID, API_HASH))

    client = TelegramClient('session',API_ID, API_HASH)
    results = []
    with open(args.outputfile, mode='w') as f:
        writer = csv.writer(f)
        if not args.noheader:
            header = ['Date', 'Sender_ID', 'Message_ID', 'Text']
            writer.writerow(header)
        with client:
            for link in tqdm(links):
                #client.loop.run_until_complete(sayhi())
                r = [preprocess(row) for row in client.loop.run_until_complete(getresults(link))]
                writer.writerows(r)  


     


