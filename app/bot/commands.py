from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "🖤 <b>AI Vision</b>\n\n"
        "Бот для генерации изображений по текстовому описанию.\n\n"
        "Скоро ты сможешь создавать AI-картинки прямо в Telegram.\n\n"
        "Напиши /help для подробностей.",
        parse_mode="HTML"
    )

@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "ℹ️ <b>Как пользоваться</b>\n\n"
        "1. Напиши описание изображения\n"
        "2. Дождись генерации\n"
        "3. Получи результат\n\n"
        "⚠️ Генерация изображений скоро будет доступна.",
        parse_mode="HTML"
    )
