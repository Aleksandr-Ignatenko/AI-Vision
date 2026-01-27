import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

from fastapi import FastAPI
import uvicorn

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 10000))

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

app = FastAPI()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🖤 <b>AI Vision</b>\n\n"
        "Привет! 👋\n"
        "Здесь ты можешь воплотить свои идеи и <b>сгенерировать изображения</b> ✨\n\n"
        "📝 Используй готовые промпты из моего канала\n"
        "или напиши <b>свой собственный</b> — я превращу его в картинку 🎨\n\n"
        "🚀 Готов начать? Просто отправь текстовый промпт",
        parse_mode="HTML"
    )


@app.get("/")
async def root():
    return {"status": "ok", "service": "ai-vision-bot"}


async def start_bot():
    await dp.start_polling(bot)


async def start_web():
    config = uvicorn.Config(app, host="0.0.0.0", port=PORT)
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    await asyncio.gather(
        start_bot(),
        start_web(),
    )


if __name__ == "__main__":
    asyncio.run(main())
