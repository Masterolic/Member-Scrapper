from pyrogram import Client
from pyrogram import filters,enums,errors
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
   DUMP_ID=environ['DUMP_ID']
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
          n=0
          print("Masterolic Member Scrapper Rolling")
          async for mem in await bot.get_chat_members(CHANNEL_ID):
                n+=
                print(n)
                try:
                   await app1.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                   
                except errors.UserAlreadyParticipant:
                    pass
                    print(f"{mem.user.id} User already Participated")
                except errors.UserChannelsTooMuch:
                    pass 
                    print(f"{mem.user.id} User Already joined In Too Many Channels")
                except errors.PeerFlood:
                    pass
                except Exception as e:
                   print(e)

if 'app1' in locals():
   app1.start()
if 'app2' in locals():
   app2.start()  
if 'app3' in locals():
   app3.start()
if 'app4' in locals():
   app4.start()  

if 'app1' in locals():
   app1.idle()
if 'app2' in locals():
   app2.idle()
if 'app3' in locals():
   app3.idle() 
if 'app4' in locals():
   app4.idle()
bot.idle()
