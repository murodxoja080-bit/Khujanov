import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import API_TOKEN

# Modullarni import qilish
import admin_panel
import ilm_markazi
import texnik_asboblar
# import music  <-- Agar music.py faylingiz bo'lsa, buni oching
# import middlewares <-- Agar middlewares.py bo'lsa, buni oching

async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=API_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    # Routerlarni ulash
    dp.include_routers(
        admin_panel.router,
        ilm_markazi.router,
        texnik_asboblar.router
        # music.router <-- Faylingiz bo'lsa, buni ham qo'shing
    )

    # Middleware ulash (agar kerak bo'lsa)
    # dp.message.middleware(middlewares.AntiFloodMiddleware())

    print(f"--- KHUJANOV TIZIMI ISHGA TUSHDI ---")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi")
