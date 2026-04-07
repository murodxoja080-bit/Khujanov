import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import API_TOKEN

# Har bir bo'limni alohida import qilamiz
import admin_panel
import ilm_markazi
import texnik_asboblar
# Agar music va middlewares fayllaringiz bo'lsa, ularni ham shu yerda import qiling:
# import music
# import middlewares

async def main():
    # 1. Loggingni sozlash
    logging.basicConfig(level=logging.INFO)

    # 2. Bot va Dispatcher obyektlarini funksiya ichida yaratish
    bot = Bot(token=API_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    # 3. Routerlarni (bo'limlarni) tartib bilan ulash
    # DIQQAT: music.router agar mavjud bo'lsa, ro'yxatga qo'shing
    dp.include_routers(
        admin_panel.router,
        ilm_markazi.router,
        texnik_asboblar.router
        # music.router 
    )

    # 4. Agar middleware bo'lsa, uni shu yerda ulaysiz:
    # dp.message.middleware(middlewares.AntiFloodMiddleware())

    print(f"--- {API_TOKEN.split(':')[0]} | KHUJANOV TIZIMI ISHGA TUSHDI ---")
    
    # 5. Botni ishga tushirish (Polling)
    # Oldingi barcha await dp.start_polling(bot) larni o'chirib, faqat shu yerda qoldiring
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        # Eng asosiysi: Faqat bitta asyncio.run(main()) bo'lishi kerak
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi")


    
