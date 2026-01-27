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
│   ├── main.py                # entry point (bot startup)
│   ├── config.py              # environment & settings
│   ├── commands.py            # commands (legacy / to be refactored)
│   │
│   └── bot/
│       ├── commands.py        # /start, /help commands
│       └── router.py          # aiogram router
│
├── .env.example               # environment variables example
├── .gitignore
├── .python-version            # Python version
├── requirements.txt           # dependencies
├── runtime.txt                # runtime config (Render)
├── README.md                  # project documentation
```
⚠️ Some files will be refactored as the project grows (queues, logging, AI integration).

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
