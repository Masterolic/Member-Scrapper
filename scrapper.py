from pyrogram import Client
from dotenv import load_dotenv
load_dotenv("config.env")
from os import environ 
if environ.get('app1'):
   app1=Client(session_string)
if environ.get('app2'):
   app2=Client(session_string)
if environ.get('app3'):
   app3=Client(session_string)
if environ.get('app4'):
   app4=Client(session_string)

try:
   OWNER_ID=environ['OWNER_ID']
   CHANNEL_ID=environ['CHANNEL_ID']
   DUMP_ID=envitorn['DUMP_ID']
   API_ID=environ['API_ID']
   API_HASH=environ['API_HASH']
   BOT_TOKEN=environ['BOT_TOKEN']
except KeyError as e:
    print(f"Madantory variables are missing {e}")
bot=Client("SCRAPER",API_ID,API_HASH,BOT_TOKEN)   

@bot.on_message(filters.command('start') & filters.user(OWNER_ID))
async def start(bot,m):
      try:
          await m.reply("starting")
          print("Masterolic Member Scrapper Rolling")
          await bot.get_chat_members(CHANNEL_ID)
      
   
