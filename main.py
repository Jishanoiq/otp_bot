# main.py

import asyncio
import aiohttp
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN, CHANNEL_ID, OTP_API_URL, OTP_API_KEY
from otp_formatter import format_otp_message

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

last_message_ids = set()

async def fetch_otp():
    headers = {"Authorization": f"Bearer {OTP_API_KEY}"}
    
    async with aiohttp.ClientSession() as session:
        async with session.get(OTP_API_URL, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("otps", [])
            else:
                return []

async def send_new_otps():
    global last_message_ids
    while True:
        otps = await fetch_otp()
        for otp in otps:
            unique_id = otp.get("id") or otp.get("code")
            if unique_id and unique_id not in last_message_ids:
                msg = format_otp_message(otp)
                await bot.send_message(chat_id=CHANNEL_ID, text=msg, disable_web_page_preview=True)
                last_message_ids.add(unique_id)
        
        await asyncio.sleep(10)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await send_new_otps()

if __name__ == "__main__":
    asyncio.run(main())
