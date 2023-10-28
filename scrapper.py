from pyrogram import Client
from pyrogram import filters,enums,errors,idle
from dotenv import load_dotenv
load_dotenv("config.env")
from os import environ 
import traceback,asyncio
if environ.get('SESSION1'):
   app1=Client(name="SCRAPPER1", session_string=environ['SESSION1'],in_memory=True)
if environ.get('SESSION2'):
   app2=Client(name="SCRAPPER2", session_string=environ['SESSION2'],in_memory=True)
if environ.get('SESSION3'):
   app3=Client(name="SCRAPPER3", session_string=environ['SESSION3'],in_memory=True)
if environ.get('SESSION4'):
   app4=Client(name="SCRAPPER4", session_string=environ['SESSION4'],in_memory=True)
if environ.get('LIMIT_COUNT'):
   LC=environ['LIMIT_COUNT']
try:
   OWNER_ID=int(environ['OWNER_ID'])
 #  CHANNEL_ID=environ['CHANNEL_ID']
   DUMP_ID=int(environ['DUMP_ID'])
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
async def add(bot,m):
      try:
          message=m
          IP=m.text.split(" ",1)
          if len(IP) == 2:
             IPT=IP[1]
          elif not m.reply_to_message:
             await m.reply("400: Bad Request Reply_To_Message To Send Message")
             return
          else:
             await m.reply("400: Bad Request Format Invalid \n eg: /add -1001744716254")
             return 
          CHANNEL_ID=int(IPT)
          try:
             await app1.start()
             if 'app2' in locals():
                await app2.start()
             if 'app3' in locals():
                await app3.start()
             if 'app4' in locals():
                await app3.start()
          except:
             pass 
          try:
             await app1.join_chat(CHANNEL_ID)
             if 'app2' in locals():     
                await app2.join_chat(CHANNEL_ID)
             if 'app3' in locals():     
                await app3.join_chat(CHANNEL_ID)
             if 'app4' in locals():     
                await app4.join_chat(CHANNEL_ID)
          except errors.PeerFlood:
              await m.reply("400: One Or More Your Accounts Can't Join Because Telegram Limited @spambot")
          except errors.UserChannelsTooMuch:
              await m.reply("400: One Or More Your Account Had Joined Too Many Groups/Channel")
          except errors.UserPrivacyRestricted:
              pass 
          except Exception as e:
              await m.reply(f"520: Error Occurred {e}")
          await m.reply("200: Masterolic Member Scrapper Rolling")
          n=0
          print("Masterolic Member Scrapper Rolling")
          async for mem in app1.get_chat_members(CHANNEL_ID):
                n+=1
                if "LC" in locals():
                   if n >= int(environ['LIMIT_COUNT']):
                      return 
                print(n)
                try:
                   if n % 4 == 1:
                      if message.reply_to_message.text:
                         await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                      elif message.reply_to_message.photo:
                          await app1.send_photo(chat_id=mem.user.id,photo=message.reply_to_message.photo.file_id,caption=message.reply_message.caption)
                         
                   elif n % 4 == 2:
                      if 'app2' in locals():
                         if message.reply_to_message.text:
                            await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                         elif message.reply_to_message.photo:
                            await app1.send_photo(chat_id=mem.user.id,photo=message.reply_to_message.photo.file_id,caption=message.reply_message.caption)
                      else:
                         if message.reply_to_message.text:
                            await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                         elif message.reply_to_message.photo:
                            await app1.send_photo(chat_id=mem.user.id,photo=message.reply_to_message.photo.file_id,caption=message.reply_message.caption)
                   elif n % 4 == 3: 
                      if 'app3' in locals():
                          if message.reply_to_message.text:
                             await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                               await app1.send_photo(chat_id=mem.user.id,photo=message.reply_to_message.photo.file_id,caption=message.reply_message.caption)
                      else:
                          if message.reply_to_message.text:
                             await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                             await app1.send_photo(chat_id=mem.user.id,photo=message.reply_to_message.photo.file_id,caption=message.reply_message.caption)
                   else:
                       if 'app4' in locals():
                          if message.reply_to_message.text:
                             await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                               await app1.send_photo(chat_id=mem.user.id,photo=message.reply_to_message.photo.file_id,caption=message.reply_message.caption)
                       else:
                            if message.reply_to_message.text:
                               await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                            elif message.reply_to_message.photo:
                               await app1.send_photo(chat_id=mem.user.id,photo=message.reply_to_message.photo.file_id,caption=message.reply_message.caption)
                   await asyncio.sleep(1)
                except errors.UserPrivacyRestricted:
                    pass 
                except errors.UserAlreadyParticipant:
                    pass
                    print(f"{mem.user.id} User already Participated")
                except errors.UserChannelsTooMuch:
                    pass 
                    print(f"{mem.user.id} User Already joined In Too Many Channels")
                except errors.FloodWait as e:
                    await asyncio.sleep(e.value)
                except errors.PeerFlood:
                    pass
                    try:
                        await app1.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                    except errors.FloodWait as e:
                      await asyncio.sleep(e.value)
                    except errors.UserPrivacyRestricted:
                        pass 
                    except errors.PeerFlood:
                        if 'app2' in locals():
                           try:
                               await app2.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                           except errors.FloodWait as e:
                              await asyncio.sleep(e.value)
                           except errors.UserPrivacyRestricted:
                               pass 
                           except errors.PeerFlood:
                               try:
                                   if 'app3' in locals():
                                      await app3.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                               except errors.FloodWait as e:
                                  await asyncio.sleep(e.value)
                               except errors.PeerFlood:
                                      try:
                                         if 'app4' in locals():
                                            await app4.add_chat_members(chat_id=DUMP_ID,user_ids=mem.user.id)
                                      except errors.FloodWait as e:
                                            await asyncio.sleep(e.value)
                                      except errors.PeerFlood:
                                          await m.reply("your current accounts are limited check @spambot")
                        else:
                           await m.reply("your current accounts are limited check @spambot")
                except Exception as e:
                   print(e)
                   print(traceback.format_exc())
      except Exception as e:
          print(e)
          print(traceback.format_exc())
          await m.reply(e)
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
