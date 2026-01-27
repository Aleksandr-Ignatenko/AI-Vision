import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

from fastapi import FastAPI
import uvicorn

from commands import BOT_COMMANDS

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

app = FastAPI()


@app.get("/")
async def healthcheck():
    return {"status": "ok"}


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🖤 *AI Vision*\n\n"
        "Бот для генерации изображений по текстовому описанию.\n\n"
        "Нажми /help, чтобы узнать, как пользоваться.",
        parse_mode="Markdown"
    )


@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "ℹ️ *Как пользоваться ботом*\n\n"
        "1️⃣ Отправь текст с описанием изображения\n"
        "2️⃣ Выбери стиль и размер (скоро)\n"
        "3️⃣ Получи сгенерированное изображение\n\n"
        "⚠️ Сейчас бот в стадии MVP.",
        parse_mode="Markdown"
    )


async def start_bot():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(BOT_COMMANDS)
    await dp.start_polling(bot)


async def start_web():
    port = int(os.environ.get("PORT", 10000))
    config = uvicorn.Config(app, host="0.0.0.0", port=port, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    await asyncio.gather(
        start_bot(),
        start_web(),
    )


if __name__ == "__main__":
    asyncio.run(main())
