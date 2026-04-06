import asyncio
from aiogram import BaseMiddleware
from aiogram.types import Message

class AntiFloodMiddleware(BaseMiddleware):
    def __init__(self, time_limit: int = 1):
        self.limit = {}
        self.time_limit = time_limit

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        if user_id in self.limit:
            return # Foydalanuvchi juda tez yozsa, javob bermaydi
        self.limit[user_id] = True
        await handler(event, data)
        await asyncio.sleep(self.time_limit)
        del self.limit[user_id]
