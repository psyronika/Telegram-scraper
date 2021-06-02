

from telethon import TelegramClient
import pandas as pd
from datetime import timedelta
import datetime

chat = 'bronvanonvoorwaardelijkeliefde'
api_id = 5521822
api_hash = '44208a895cc9a3ed25eb161e9eaad9f7'
client = TelegramClient('session_id', api_id, api_hash)

# Note `async with` and `async for`
	result = []
	async for msg in client.iter_messages(chat, limit = 5000): 
		result.append([msg.date, msg.sender.first_name, msg.id, msg.text])

df = pd.DataFrame(result, columns = ['Date', 'Name', 'ID', 'Text'])
df.to_csv(r'/Users/m.simonuva.nl/Documents/PhD project files/data_new.csv', index = False)

#does not work yet

date = datetime.date.today()
async def get_messages_at_date(chat, date):
    results = []
    year= date + datetime.timedelta(days=1)
    async for msg in client.iter_messages(chat, offset_date=date):
        if msg.date < date:
            return results
        results.append(msg)

await client.disconnect()