import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from fastapi import FastAPI
import uvicorn

from commands import BOT_COMMANDS
from bot.router import router as bot_router

load_dotenv()

# -------------------------
# Config
# -------------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

# -------------------------
# Telegram
# -------------------------
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# подключаем ВСЕ роутеры бота
dp.include_router(bot_router)

# -------------------------
# Web (for Render healthcheck)
# -------------------------
app = FastAPI()

@app.api_route("/", methods=["GET", "HEAD"])
async def healthcheck():
    return {"status": "ok"}


# -------------------------
# Startup tasks
# -------------------------
async def start_bot():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(BOT_COMMANDS)
    await dp.start_polling(bot)

async def start_web():
    port = int(os.environ.get("PORT", 10000))
    config = uvicorn.Config(
        app=app,
        host="0.0.0.0",
        port=port,
        log_level="info",
    )
    server = uvicorn.Server(config)
    await server.serve()

# -------------------------
# Main entrypoint
# -------------------------
async def main():
    await asyncio.gather(
        start_bot(),
        start_web(),
    )

if __name__ == "__main__":
    asyncio.run(main())
