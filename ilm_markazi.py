import aiohttp
from bs4 import BeautifulSoup
from aiogram import Router, F, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SIGNATURE, DIVIDER, LIBRARY_URL

router = Router()

# ————————————— AVTOMATIK QIDIRUV FUNKSIYASI —————————————
async def fetch_educational_data(query):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{LIBRARY_URL}{query}") as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                results = soup.find_all('h3', class_='entry-title', limit=3)
                if results:
                    links = [f"📖 <a href='{r.find('a')['href']}'>{r.text.strip()}</a>" for r in results]
                    return "\n\n".join(links)
    return None

# ————————————— ILM MARKAZI ASOSIY MENYUSI —————————————
@router.callback_query(F.data == "open_ilm")
async def ilm_main_menu(callback: types.CallbackQuery):
    text = (
        f"🎓 <b>ILM VA TA'LIM MARKAZI</b>\n"
        f"📍 <i>Bosh sahifa > Ilm Markazi</i>\n"
        f"{DIVIDER}\n"
        f"Bu yerda Maktab (1-11), OTM va Kengaytirilgan kutubxona resurslari jamlangan.\n\n"
        f"📚 <b>Bo'limni tanlang:</b>"
        f"{SIGNATURE}"
    )
    markup = InlineKeyboardMarkup(inline_keyboard=,,
    ])
    await callback.message.edit_text(text, reply_markup=markup)

# ————————————— MAKTAB BO'LIMI (AVTOMATIK) —————————————
@router.callback_query(F.data == "ilm_maktab")
async def school_section(callback: types.CallbackQuery):
    text = (
        f"🏫 <b>MAKTAB AKADEMIYASI</b>\n"
        f"{DIVIDER}\n"
        f"Sizga qaysi sinf darsligi kerak? Fan va sinfni yozib yuboring.\n"
        f"<i>Masalan: Fizika 9-sinf</i>"
        f"{SIGNATURE}"
    )
    await callback.message.edit_text(text, reply_markup=InlineKeyboardMarkup(inline_keyboard=
    ]))

# ————————————— QIDIRUVNI QABUL QILISH —————————————
@router.message(F.text)
async def handle_search(message: types.Message):
    # Bu qism foydalanuvchi yozgan fanni avtomatik qidiradi
    await message.answer("🔍 <b>Khujanov Tizimi qidirmoqda...</b>")
    results = await fetch_educational_data(message.text)
    
    if results:
        await message.answer(f"📚 <b>Topilgan darsliklar va materiallar:</b>\n\n{results}{SIGNATURE}")
    else:
        await message.answer(f"🤖 <b>Ma'lumot topilmadi.</b>\nLekin AI orqali yordam berishim mumkin!{SIGNATURE}")
