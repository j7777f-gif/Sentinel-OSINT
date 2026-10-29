# Sentinel-OSINT

A Python Telegram bot for IP information lookup and geolocation.

## Features
- `/start` - Check bot status.
- `/ip <IP_ADDRESS>` - Get available IP details.
- `/geo <IP_ADDRESS>` - Get geolocation details and a Google Maps link.

## Technologies
- Python
- aiogram
- aiohttp
- python-dotenv

## Setup
1. Create a virtual environment:
   `python3 -m venv venv`

2. Activate it:
   `source venv/bin/activate`

3. Install dependencies:
   `pip install -r requirements.txt`

4. Create a `.env` file and add:
   `BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN`

5. Run the bot:
   `python bot.py`

## Security
Never upload your `.env` file or expose your Telegram bot token.

## Disclaimer
For educational purposes and authorized security research.
