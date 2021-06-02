

from telethon import TelegramClient
import pandas as pd
import datetime

chat = 'FVDNL'#works with channels where not subscribed
api_id = 5521822
api_hash = '44208a895cc9a3ed25eb161e9eaad9f7'
client = TelegramClient('session_id', api_id, api_hash)

# Note `async with` and `async for`
async with client:
	result = []
	async for msg in client.iter_messages(chat): 
		result.append([msg.date, msg.sender_id, msg.id, msg.text])

df = pd.DataFrame(result, columns = ['Date', 'Sender_ID','Message_ID', 'Text'])
df.to_csv(r'/Users/m.simonuva.nl/Documents/GitHub/Telegram-scraper/channel.csv', index = False)




#gethistoryrequest
#detailed output, very limited though
with TelegramClient('name', api_id, api_hash) as client:
    result = client(functions.messages.GetHistoryRequest(
        peer='GroenLinks',
        offset_id=0,
        offset_date=datetime.datetime(2021, 6, 1),
        add_offset=0,
        limit=1,
        max_id=0,
        min_id=0,
        hash=0
    ))
    print(result.stringify())