

from telethon import TelegramClient
import pandas as pd


#chat = 'bronvanonvoorwaardelijkeliefde'
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

# Note `async with` and `async for`
async with client:
	result = []
	async for msg in client.iter_messages(chat): #worked without limit for group
		result.append([msg.date, msg.sender_id, msg.id, msg.text])

df = pd.DataFrame(result, columns = ['Date', 'Sender_ID', 'Message_ID', 'Text'])
df.to_csv(r'/Users/m.simonuva.nl/Documents/GitHub/Telegram-scraper/testing.csv', index = False)

