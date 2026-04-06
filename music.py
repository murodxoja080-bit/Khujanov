from aiogram import Router, F, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SIGNATURE, DIVIDER

router = Router()

@router.callback_query(F.data == "ilm_audio")
async def music_menu(callback: types.CallbackQuery):
    text = (
        f"🎧 <b>AUDIO KUTUBXONA</b>\n"
        f"{DIVIDER}\n"
        f"Siz bu yerda audio kitoblar va ilmiy darslarni topishingiz mumkin.\n\n"
        f"🎵 <b>Musiqa yoki audio kitob nomini yozing:</b>"
        f"{SIGNATURE}"
    )
    await callback.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=
    ]))

# Musiqa qidiruv algoritmi (YouTube API orqali bog'lanadi)
@router.message(F.text.startswith("m:")) # Masalan 'm:Sherali' deb yozsa
async def find_music(message: types.Message):
    query = message.text.replace("m:", "")
    await message.answer(f"🔎 <b>{query}</b> bo'yicha audio qidirilmoqda...")
    # Bu yerda musiqa ssilkasini yuborish kodi bo'ladi
