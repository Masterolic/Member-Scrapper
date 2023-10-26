from pyrogram import Client
from pyrogram import filters,enums,errors,idle
from dotenv import load_dotenv
load_dotenv("config.env")
from os import environ 
if environ.get('SESSION1'):
   app1=Client(name="SCRAPPER1", session_string=session_string,in_memory=True)
if environ.get('SESSION2'):
   app2=Client(name="SCRAPPER2", session_string=session_string,in_memory=True)
if environ.get('SESSION3'):
   app3=Client(name="SCRAPPER3", session_string=session_string,in_memory=True)
if environ.get('SESSION4'):
   app4=Client(name="SCRAPPER4", session_string=session_string,in_memory=True)

try:
   OWNER_ID=environ['OWNER_ID']
 #  CHANNEL_ID=environ['CHANNEL_ID']
   DUMP_ID=environ['DUMP_ID']
   API_ID=environ['API_ID']
   API_HASH=environ['API_HASH']
   BOT_TOKEN=environ['BOT_TOKEN']
   environ['SESSION1']
except KeyError as e:
    print(f"Madantory variables are missing {e}")
bot=Client("SCRAPER",api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN,in_memory=True)   

@bot.on_message(filters.command('start'))
async def start(bot,m):
      await m.reply(f"Hey {m.from_user.first_name} A Simple Telegram Bot For Scraping Members")
   
@bot.on_message(filters.command('add') & filters.user(OWNER_ID))
async def add(bot,m)
      try:
          IP=m.text.split(" ",1)
          if len(IP) == 2:
             IPT=IP[1]
          else:
             await m.reply("400: Bad Request Format Invalid \n eg: /add -1001744716254")
             return 
          CHANNEL_ID=int(IPT)
          await m.reply("Masterolic Member Scrapper Rolling")
          n=0
          print("Masterolic Member Scrapper Rolling")
          async for mem in app1.get_chat_members(CHANNEL_ID):
                n+=1
                print(n)
                try:
                   if n % 4 == 1:
                      await app1.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                   elif n % 4 == 2:
                      if 'app2' in locals():
                         await app2.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                      else:
                         await app1.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                   elif n % 4 == 3: 
                      if 'app3' in locals():
                          await app3.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                      else:
                          await app1.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                   else:
                       if 'app4' in locals():
                          await app4.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                       else:
                            await app1.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                except errors.UserAlreadyParticipant:
                    pass
                    print(f"{mem.user.id} User already Participated")
                except errors.UserChannelsTooMuch:
                    pass 
                    print(f"{mem.user.id} User Already joined In Too Many Channels")
                except errors.PeerFlood:
                    pass
                    try:
                        await app1.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                    except errors.PeerFlood:
                        if 'app2' in locals():
                           try:
                               await app2.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                           except errors.PeerFlood:
                               try:
                                   if 'app3' in locals():
                                      await app3.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                               except errors.PeerFlood:
                                      try:
                                         if 'app4' in locals():
                                            await app4.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                                      except errors.PeerFlood:
                                          await m.reply("your current accounts are limited check @spambot")
                        else:
                           await m.reply("your current accounts are limited check @spambot")
                except Exception as e:
                   print(e)
                   await message.reply(e)
      except Exception as e:
          print(e)
if __name__ == '__main__':
   bot.start()   
   bt=bot.get_me()
   print(bt.username)
   if 'app1' in locals():
      app1.start()
      ap1=app1.get_me()
      print(ap1.first_name)
   if 'app2' in locals():
      app2.start() 
      ap2=app2.get_me()
      print(ap2.first_name)
   if 'app3' in locals():
      app3.start()
      ap3=app3.get_me()
      print(ap3.first_name)
   if 'app4' in locals():
      app4.start()
      ap4=app4.get_me()
      print(ap4.first_name)

if 'app1' in locals():
   app1.stop()
if 'app2' in locals():
   app2.stop()
if 'app3' in locals():
   app3.stop() 
if 'app4' in locals():
   app4.stop()
idle()
