from pyrogram import Client
from pyrogram import filters,enums,errors
from dotenv import load_dotenv
load_dotenv("config.env")
from os import environ 
if environ.get('SESSION1'):
   app1=Client(name="SCRAPPER1", session_string=session_string)
if environ.get('SESSION2'):
   app2=Client(name="SCRAPPER2", session_string=session_string)
if environ.get('SESSION3'):
   app3=Client(name="SCRAPPER3", session_string=session_string)
if environ.get('SESSION4'):
   app4=Client(name="SCRAPPER4", session_string=session_string)

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
                n+=1
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
if __name__ == '__main__':
   bot.start()
   bt=print(bt.username)
   if 'app1' in locals():
      app1.start()
   if 'app2' in locals():
      app2.start()  
   if 'app3' in locals():
      app3.start()
   if 'app4' in locals():
      app4.start()  

if 'app1' in locals():
      app1.stop()
if 'app2' in locals():
   app2.stop()
if 'app3' in locals():
   app3.stop() 
if 'app4' in locals():
   app4.stop()
