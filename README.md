# 🖤 AI Vision

Telegram bot for AI-powered image generation.

## Status
🚧 MVP in progress

## Tech Stack
- Python
- aiogram
- Telegram Bot API
- Gemini / Imagen (planned)
- Render (hosting)
- Supabase (database, planned)
- Vercel (landing/admin, planned)

## Project Structure (MVP-ready)

```text
ai-vision-bot/
│
├── app/
│ ├── init.py # ✅ app package
│ ├── main.py # ✅ entry point (bot startup)
│ ├── config.py # ✅ environment & settings
│ │
│ ├── bot/
│ │ ├── init.py # ✅ bot package
│ │ ├── commands.py # ✅ /start, /help commands
│ │ └── router.py # ✅ aiogram router
│ │
│ └── utils/
│ └── logger.py # 🕒 logging utilities (planned)
│
├── .env.example # ✅ environment variables example
├── requirements.txt # ✅ dependencies
├── README.md # ✅ project documentation
└── render.yaml # 🕒 deployment config (planned)ai-vision-bot/
│
├── app/
│ ├── init.py # ✅ app package
│ ├── main.py # ✅ entry point (bot startup)
│ ├── config.py # ✅ environment & settings
│ │
│ ├── bot/
│ │ ├── init.py # ✅ bot package
│ │ ├── commands.py # ✅ /start, /help commands
│ │ └── router.py # ✅ aiogram router
│ │
│ └── utils/
│ └── logger.py # 🕒 logging utilities (planned)
│
├── .env.example # ✅ environment variables example
├── requirements.txt # ✅ dependencies
├── README.md # ✅ project documentation
└── render.yaml # 🕒 deployment config (planned)
```
**Legend:**
- ✅ implemented
- 🚧 in progress
- 🕒 planned

## Commands
- `/start` — bot introduction
- `/help` — usage instructions

## Roadmap
- [x] Project setup
- [x] Telegram bot created
- [x] Repository & base architecture
- [x] Basic bot commands (`/start`, `/help`)
- [ ] Image generation (Gemini)
- [ ] User limits & billing & request queue
- [ ] Logging & cost tracking
- [ ] Admin panel

---
Made with 🖤
