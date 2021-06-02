

from telethon import TelegramClient
import pandas as pd
from datetime import timedelta
import datetime

chat = 'GroenLinks'
api_id = 5521822
api_hash = '44208a895cc9a3ed25eb161e9eaad9f7'
client = TelegramClient('session_id', api_id, api_hash)

# Note `async with` and `async for`
async with client:
	result = []
	async for msg in client.iter_messages(chat, limit = None): 
		result.append([msg.date, msg.id, msg.text])

df = pd.DataFrame(result, columns = ['Date', 'ID', 'Text'])
df.to_csv(r'/Users/m.simonuva.nl/Documents/PhD project files/Telegram/channel.csv', index = False)
