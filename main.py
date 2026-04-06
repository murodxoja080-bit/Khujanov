import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import API_TOKEN

# Har bir bo'limni alohida import qilamiz
# (Bu fayllarni hozir yaratamiz)
import admin_panel, ilm_markazi, texnik_asboblar

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=API_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    # Bo'limlarni (Routerlarni) tartib bilan ulash
    dp.include_routers(
        admin_panel.router,
        ilm_markazi.router,
        texnik_asboblar.router
    )

    print(f"--- {API_TOKEN.split(':')[0]} | KHUJANOV TIZIMI ISHGA TUSHDI ---")
    await dp.start_polling(bot)

# 25-qatordan boshlab hammasini o'chirib, buni qo'ying:

async def main():
    # Barcha routerlarni va middlewarelarni shu yerda ro'yxatdan o'tkazamiz
    dp.include_routers(
        admin_panel.router,
        ilm_markazi.router,
        texnik_asboblar.router,
        music.router  # Music routerni ham shu yerga qo'shdik
    )
    
    # Agar middleware bo'lsa, uni ham shu yerda ko'rsatamiz
    # dp.message.middleware(middleware_nomi) 

    print("--- Bot muvaffaqiyatli ishga tushdi ---")
    
    # Botni ishga tushirish (Polling)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    # Qavslar bilan (main()) yozilishi shart!
    asyncio.run(main())

    
