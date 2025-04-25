# Leboncoin Apartment Bot

This bot monitors new apartment listings in Cagnes-sur-Mer on Leboncoin and sends alerts to Telegram.

## Setup

1. Create a `.env` file or set environment variables on Render:
   - `TELEGRAM_TOKEN` = your Telegram bot token
   - `TELEGRAM_CHAT_ID` = your Telegram user ID

2. Run with Python 3.8+

## Deploy to Render

- Create a new **Background Worker** on [Render.com](https://render.com)
- Connect your GitHub repo
- Set environment variables in the "Environment" tab
- Use this start command:
  
  ```bash
  python main.py
