import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from KIGO import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID

DEADLY_IMG = ALIVE_PIC if ALIVE_PIC else "http://telegra.ph//file/ba9cdb63f6f1a18fd57d1.png"

Deadly_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/kigo_omfo")
        ],
        [
        Button.url("• ᴍᴀɪɴᴛᴀɪɴ ʙʏ •", "https://t.me/Shubhanshutya")
        ]
        ]
               
DeadlyX_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/kigo_omfo"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/godzilla_chatting")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/Nonsensexdd/Godzillaxspam")
        ]
        ]
        
        
#USERS 


@BOT0.on(events.NewMessage(pattern="/start"))
@BOT1.on(events.NewMessage(pattern="/start"))
@BOT2.on(events.NewMessage(pattern="/start"))
@BOT3.on(events.NewMessage(pattern="/start"))
@BOT4.on(events.NewMessage(pattern="/start"))
@BOT5.on(events.NewMessage(pattern="/start"))
@BOT6.on(events.NewMessage(pattern="/start"))
@BOT7.on(events.NewMessage(pattern="/start"))
@BOT8.on(events.NewMessage(pattern="/start"))
@BOT9.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DeadlyBot = await event.client.get_me()
       bot_id = DeadlyBot.first_name
       bot_username = DeadlyBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheDeadly = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheDeadly,
                  DEADLY_IMG,
                  caption=ownermsg, 
                  buttons=Deadly_Button)
       else:
            await event.client.send_file(TheDeadly,
                  DEADLY_IMG,
                  caption=usermsg, 
                  buttons=DeadlyX_Button)
                
