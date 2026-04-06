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

if __name__ == "__main__":
    asyncio.run(main)
    from handlers import music, middlewares
# ...
dp.message.middleware(middlewares.AntiFloodMiddleware)
dp.include_router(music.router)
