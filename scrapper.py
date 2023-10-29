from pyrogram import Client
from pyrogram import filters,enums,errors,idle
from dotenv import load_dotenv
load_dotenv("config.env")
from os import environ , remove 
import traceback,asyncio
if environ.get('SESSION1'):
   app1=Client(name="SCRAPPER1", session_string=environ['SESSION1'],in_memory=True)
if environ.get('SESSION2'):
   app2=Client(name="SCRAPPER2", session_string=environ['SESSION2'],in_memory=True)
if environ.get('SESSION3'):
   app3=Client(name="SCRAPPER3", session_string=environ['SESSION3'],in_memory=True)
if environ.get('SESSION4'):
   app4=Client(name="SCRAPPER4", session_string=environ['SESSION4'],in_memory=True)
if environ.get('SESSION5'):
   app1=Client(name="SCRAPPER5", session_string=environ['SESSION5'],in_memory=True)
if environ.get('SESSION6'):
   app2=Client(name="SCRAPPER6", session_string=environ['SESSION6'],in_memory=True)
if environ.get('SESSION7'):
   app3=Client(name="SCRAPPER7", session_string=environ['SESSION7'],in_memory=True)
if environ.get('SESSION8'):
   app4=Client(name="SCRAPPER8", session_string=environ['SESSION8'],in_memory=True) 
if environ.get('SESSION9'):
   app1=Client(name="SCRAPPER9", session_string=environ['SESSION9'],in_memory=True)
if environ.get('SESSION10'):
   app2=Client(name="SCRAPPER10", session_string=environ['SESSION10'],in_memory=True)
if environ.get('LIMIT_COUNT'):
   LC=environ['LIMIT_COUNT']
try:
   OWNER_ID=int(environ['OWNER_ID'])
   CHANNEL_ID=int(environ['CHANNEL_ID'])
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
          else:
             IPT=0
          if not m.reply_to_message:
             await m.reply("400: Bad Request Reply_To_Message To Send Message")
             return
      #    else:
      #        await m.reply("400: Bad Request Format Invalid \n eg: /add -1001744716254")
      #       return 
          if message.reply_to_message.photo:
             path=await bot.download_media(message.reply_to_message.photo.file_id)
          CHANNEL_ID=int(IPT)
          try:
             await app1.start()
             if 'app2' in locals():
                await app2.start()
             if 'app3' in locals():
                await app3.start()
             if 'app4' in locals():
                await app4.start()
             if 'app5' in locals():
                await app5.start()
             if 'app6' in locals():
                await app6.start()
             if 'app7' in locals():
                await app7.start()
             if 'app8' in locals():
                await app8.start()
             if 'app9' in locals():
                await app9.start()
             if 'app10' in locals():
                await app10.start()
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
                if not n >= IPT:
                   continue 
                if "LC" in locals():
                   if n >= int(environ['LIMIT_COUNT']):
                      return 
                print(n)
                try:
                   if n % 9 == 1:
                      if message.reply_to_message.text:
                         await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                      elif message.reply_to_message.photo:
                         # path=await bot.download_media(message.reply_to_message.photo.file_id)
                          await app1.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                         
                   elif n % 9 == 2:
                      if 'app2' in locals():
                         if message.reply_to_message.text:        
                            await app2.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                         elif message.reply_to_message.photo:
                       #     path=await bot.download_media(message.reply_to_message.photo.file_id)
                            await app2.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                      else:
                         if message.reply_to_message.text:
                            await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                         elif message.reply_to_message.photo:
                      #      path=await bot.download_media(message.reply_to_message.photo.file_id)
                            await app1.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                   elif n % 9 == 3: 
                      if 'app3' in locals():
                          if message.reply_to_message.text:
                             await app3.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                    #           path=await bot.download_media(message.reply_to_message.photo.file_id)
                               await app3.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                      else:
                          if message.reply_to_message.text:
                             await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                     #        path=await bot.download_media(message.reply_to_message.photo.file_id)
                             await app1.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                   elif n % 9 == 4: 
                      if 'app4' in locals():
                          if message.reply_to_message.text:
                             await app4.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                    #           path=await bot.download_media(message.reply_to_message.photo.file_id)
                               await app4.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                      else:
                          if message.reply_to_message.text:
                             await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                     #        path=await bot.download_media(message.reply_to_message.photo.file_id)
                             await app1.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                   elif n % 9 == 5: 
                      if 'app5' in locals():
                          if message.reply_to_message.text:
                             await app5.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                    #           path=await bot.download_media(message.reply_to_message.photo.file_id)
                               await app5.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                      else:
                          if message.reply_to_message.text:
                             await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                     #        path=await bot.download_media(message.reply_to_message.photo.file_id)
                             await app1.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                   elif n % 9 == 6: 
                      if 'app6' in locals():
                          if message.reply_to_message.text:
                             await app6.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                    #           path=await bot.download_media(message.reply_to_message.photo.file_id)
                               await app6.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                      else:
                          if message.reply_to_message.text:
                             await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                     #        path=await bot.download_media(message.reply_to_message.photo.file_id)
                             await app1.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                   elif n % 9 == 7: 
                      if 'app7' in locals():
                          if message.reply_to_message.text:
                             await app7.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                    #           path=await bot.download_media(message.reply_to_message.photo.file_id)
                               await app7.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                      else:
                          if message.reply_to_message.text:
                             await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                     #        path=await bot.download_media(message.reply_to_message.photo.file_id)
                             await app1.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                   elif n % 9 == 8: 
                      if 'app8' in locals():
                          if message.reply_to_message.text:
                             await app8.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                    #           path=await bot.download_media(message.reply_to_message.photo.file_id)
                               await app8.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                      else:
                          if message.reply_to_message.text:
                             await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                     #        path=await bot.download_media(message.reply_to_message.photo.file_id)
                             await app1.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                   elif n % 9 == 9: 
                      if 'app9' in locals():
                          if message.reply_to_message.text:
                             await app9.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                    #           path=await bot.download_media(message.reply_to_message.photo.file_id)
                               await app9.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                      else:
                          if message.reply_to_message.text:
                             await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                     #        path=await bot.download_media(message.reply_to_message.photo.file_id)
                             await app1.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                   else:
                       if 'app10' in locals():
                          if message.reply_to_message.text:
                             await app10.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                          elif message.reply_to_message.photo:
                      #         path=await bot.download_media(message.reply_to_message.photo.file_id)
                               await app10.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                       else:
                            if message.reply_to_message.text:
                               await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                            elif message.reply_to_message.photo:
                      #         path=await bot.download_media(message.reply_to_message.photo.file_id)
                               await app1.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)     
                   await asyncio.sleep(0.1)
                   continue 
                except errors.UserPrivacyRestricted:
                    pass 
                except errors.UserAlreadyParticipant:
                    pass
                    print(f"{mem.user.id} User already Participated")
                except errors.UserChannelsTooMuch:
                    pass 
                    print(f"{mem.user.id} User Already joined In Too Many Channels")
                except (errors.PeerFlood,errors.FloodWait):
                    pass
                    try:
                        if message.reply_to_message.text:
                             await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                        elif message.reply_to_message.photo:
                      #         path=await bot.download_media(message.reply_to_message.photo.file_id)
                             await app1.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
   
                    except errors.UserPrivacyRestricted:
                        pass 
                    except (errors.PeerFlood,errors.FloodWait):
                        if 'app2' in locals():
                           try:
                               if message.reply_to_message.text:
                                  await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                               elif message.reply_to_message.photo:
                      #         path=await bot.download_media(message.reply_to_message.photo.file_id)
                                  await app1.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                           
                           except errors.UserPrivacyRestricted:
                               pass 
                           except (errors.PeerFlood,errors.FloodWait):
                               try:
                                   if 'app3' in locals():
                                      if message.reply_to_message.text:
                                         await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                                      elif message.reply_to_message.photo:
                      #         path=await bot.download_media(message.reply_to_message.photo.file_id)
                                         await app1.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                               
                               except (errors.PeerFlood,errors.FloodWait):
                                      try:
                                         if 'app4' in locals():
                                            if message.reply_to_message.text:
                                                await app1.send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                                            elif message.reply_to_message.photo:
                      #         path=await bot.download_media(message.reply_to_message.photo.file_id)
                                                await app1.send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                                      
                                      except (errors.PeerFlood,errors.FloodWait):
                                          get_bool=True 
                                          for i in range(11):
                                              if get_bool:
                                                 try:
                                                     if message.reply_to_message.text:
                                                        await app[i].send_message(chat_id=mem.user.id,text=m.reply_to_message.text)
                                                     elif message.reply_to_message.photo:
                      #         path=await bot.download_media(message.reply_to_message.photo.file_id)
                                                         await app[i].send_photo(chat_id=mem.user.id,photo=path,caption=message.reply_to_message.caption)
                                                     get_bool=True
                                                 except:
                                                     pass
                                          if not get_bool:
                                             return await m.reply("your current accounts are limited check @spambot")
                        else:
                           return await m.reply("your current accounts are limited check @spambot")
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
   if 'app5' in locals():
      app5.start()
      ap5=app5.get_me()
      print(ap5.first_name)
   if 'app6' in locals():
      app6.start()
      ap6=app6.get_me()
      print(ap6.first_name)
   if 'app7' in locals():
      app7.start()
      ap7=app7.get_me()
      print(ap4.first_name)
   if 'app8' in locals():
      app8.start()
      ap8=app8.get_me()
      print(ap8.first_name)
   if 'app9' in locals():
      app9.start()
      ap9=app9.get_me()
      print(ap9.first_name)
   if 'app10' in locals():
      app10.start()
      ap10=app10.get_me()
      print(ap10.first_name)
if 'app1' in locals():
   app1.stop()
if 'app2' in locals():
   app2.stop()
if 'app3' in locals():
   app3.stop() 
if 'app4' in locals():
   app4.stop()
if 'app5' in locals():
   app5.stop()
if 'app6' in locals():
   app6.stop()
if 'app7' in locals():
   app7.stop() 
if 'app8' in locals():
   app8.stop()
if 'app9' in locals():
   app9.stop()
if 'app10' in locals():
   app10.stop()  
idle()
   
