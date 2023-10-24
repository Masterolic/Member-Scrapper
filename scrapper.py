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


