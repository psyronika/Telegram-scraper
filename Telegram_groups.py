

from telethon import TelegramClient
import pandas as pd
import asyncio


chat = 'wilderspvv'
api_id = 5521822
api_hash = '44208a895cc9a3ed25eb161e9eaad9f7'
#client = TelegramClient('test', api_id, api_hash)

'''
#source = pd.read_csv('/Users/m.simonuva.nl/Documents/GitHub/Telegram-scraper/Telegram-scraper/Telegram_chats.csv')
chats = source['links'].tolist()

async def get_chat(chats):
	for chat in chats:
		print(chat)
'''
# Note `async with` and `async for`

#try to get event loop
def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()

# if not event loop create new
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

#conect to client
client = TelegramClient('session_name', api_id, api_hash)
client.start()

'''
async def main():
	try:
		await client.connect()
	except OSError:
		print('Failed to connect')
'''
# get message date, sender id, message id, message text

async with client:
	result = []
	async for msg in client.iter_messages(chat): #worked without limit for group
		result.append([msg.date, msg.sender_id, msg.id, msg.text])

df = pd.DataFrame(result, columns = ['Date', 'Sender_ID', 'Message_ID', 'Text'])
df.to_csv(r'/Users/m.simonuva.nl/Documents/GitHub/Telegram-scraper/geert.csv', index = False)

