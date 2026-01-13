import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.utils import executor

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

async def autopost():
    while True:
        await bot.send_message(CHANNEL_ID, "😂 Анекдот скоро")
        await asyncio.sleep(1800)

async def on_startup(_):
    asyncio.create_task(autopost())

executor.start_polling(dp, on_startup=on_startup)
