from aiogram import Router, F, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SIGNATURE, DIVIDER

router = Router()

@router.callback_query(F.data == "open_tools")
async def tools_main_menu(callback: types.CallbackQuery):
    text = (
        f"🛠 <b>UNIVERSAL TEXNIK ASBOBLAR</b>\n"
        f"📍 <i>Bosh sahifa > Texnik Asboblar</i>\n"
        f"{DIVIDER}\n"
        f"Sun'iy intellekt (AI), Video yuklovchi va multimedia tahrirlovchi xizmatlar."
        f"{SIGNATURE}"
    )
    markup = InlineKeyboardMarkup(inline_keyboard=,,
    ])
    await callback.message.edit_text(text, reply_markup=markup)

@router.callback_query(F.data == "tool_ai")
async def ai_assistant(callback: types.CallbackQuery):
    await callback.message.edit_text(
        f"🤖 <b>AI AQLLI USTOZ</b>\n{DIVIDER}\nHar qanday savolingizni yozib yuboring, men tahlil qilaman...{SIGNATURE}",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=])
    )
