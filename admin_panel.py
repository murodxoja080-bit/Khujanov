from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMIN_ID, BRAND, DIVIDER, SIGNATURE

router = Router()

@router.message(Command("admin"))
async def founder_panel(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        text = (
            f"🛡 <b>{BRAND} | NAZORAT MARKAZI</b>\n"
            f"{DIVIDER}\n"
            f"Xush kelibsiz, <b>{BRAND} Founder!</b>\n"
            f"Tizim 100% nazorat ostida.\n\n"
            f"📊 <b>Statistika:</b> 12,450 foydalanuvchi\n"
            f"📡 <b>Server:</b> 0.4ms"
            f"{SIGNATURE}"
        )
        markup = InlineKeyboardMarkup(inline_keyboard=,,
        ])
        await message.answer(text, reply_markup=markup)
