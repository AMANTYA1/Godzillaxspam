import os
import asyncio
import sys
import git
import heroku3
# Changed root to Godfather
from KIGO import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9
from KIGO import OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, deadlyversion
from KIGO import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
# alive Pic By Default It's Will Show Our
from KIGO import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

ZAID_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/c6f99c0b68ff07439ed72.jpg"
  

DEADLY = "โฏ ๐๐ถ๐ด๐ผ ๐ฆ๐ฝ๐ฎ๐บ ๐๐ฒ๐ฟ๐ฒ โฏ\n\n"
DEADLY += f"โโโโโโโโโโโโโโโโโโโ\n"
DEADLY += f"โข **แดสแดสแดษด แด แดสsษชแดษด** : `3.10.1`\n"
DEADLY += f"โข **แดแดสแดแดสแดษด แด แดสsษชแดษด** : `{version.__version__}`\n"
DEADLY += f"โข **๐๐ถ๐ด๐๐ผ๐ แด แดสsษชแดษด**  : `{Kigoversion}`\n"
DEADLY += f"โโโโโโโโโโโโโโโโโโโ\n\n"   

                                  
@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await SAM.send_file(event.chat_id,
                                  ZAID_PIC,
                                  caption=deadly,
                                  buttons=[
        [
        Button.url("แดสแดษดษดแดส", "https://t.me/kigo_omfo"),
        Button.url("sแดแดแดแดสแด", "https://t.me/godzilla_chatting")
        ],
        [
        Button.url("โข สแดแดแด โข", "https://github.com/Nonsensexdd/Godzillaxspam")
        ]
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"๐ ๐ตโ๐ดโ๐ณโ๐ฌโ!\n\nโก๏ธ `{ms}` ๐บ๐ โก๏ธ")
        
        

@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**Rebooting โช๏ธ**.. Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await BOT0.disconnect()
        except Exception:
            pass
        try:
            await BOT1.disconnect()
        except Exception:
            pass
        try:
            await BOT2.disconnect()
        except Exception:
            pass
        try:
            await BOT3.disconnect()
        except Exception:
            pass
        try:
            await BOT4.disconnect()
        except Exception:
            pass
        try:
            await BOT5.disconnect()
        except Exception:
            pass
        try:
            await BOT6.disconnect()
        except Exception:
            pass
        try:
            await BOT7.disconnect()
        except Exception:
            pass
        try:
            await BOT8.disconnect()
        except Exception:
            pass
        try:
            await BOT9.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

# this Feature Will Works only If u r Added Heroku api
@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Adding user as a sudo...")
        DEADLY = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added `{target}` ** as a sudo user ๐ฑ Restarting.. Please wait a minute...")
        heroku_var[DEADLY] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
