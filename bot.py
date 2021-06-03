import discord
from ahk import AHK
from dotenv import load_dotenv
from os import environ

load_dotenv()

client = discord.Client()

TOKEN = environ.get("TOKEN")
AHK_PATH = environ.get("AHK_PATH")

ahk = AHK(executable_path=AHK_PATH)

@client.event
async def on_ready():
    print(f"Login worked, user is: {client.user}")

@client.event
async def on_message(message):
    if message.content == "!switch":
        ahk.send_input("{Shift down}{F1 down}")
        ahk.send_input("{Shift up}{F1 up}")

client.run(TOKEN)
