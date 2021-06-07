

from telethon import TelegramClient
import pandas as pd
import asyncio


chat = 'https://t.me/geertwildersss'
api_id = 5521822
api_hash = '44208a895cc9a3ed25eb161e9eaad9f7'
client = TelegramClient('session', api_id, api_hash)

'''
source = pd.read_csv('/Users/m.simonuva.nl/Documents/GitHub/Telegram-scraper/Telegram-scraper/Telegram_chats.csv')
chats = source['links'].tolist()

async def get_chat(chats):
	for chat in chats:
		print(chat)
'''

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


client = TelegramClient('session_name', api_id, api_hash)
client.start()

# Note `async with` and `async for`
async with client:
	result = []
	async for msg in client.iter_messages(chat): #worked without limit for group
		result.append([msg.date, msg.sender_id, msg.id, msg.text])
client.run_until_disconnected()

df = pd.DataFrame(result, columns = ['Date', 'Sender_ID', 'Message_ID', 'Text'])
df.to_csv(r'/Users/m.simonuva.nl/Documents/GitHub/Telegram-scraper/wilder.csv', index = False)


