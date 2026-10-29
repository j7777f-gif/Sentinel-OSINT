import asyncio
import aiohttp

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    print("/start received")
    await message.answer("✅ البوت يعمل بنجاح")


@dp.message(Command("ip"))
async def ip_lookup(message: Message):
    print("IP command received:", message.text)

    args = message.text.split()

    if len(args) < 2:
        await message.answer("الاستخدام:\n/ip 8.8.8.8")
        return

    ip = args[1]

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://ip-api.com/json/{ip}") as response:
                data = await response.json()

        print(data)

        await message.answer(
            f"""🌍 IP: {data['query']}
🏳 الدولة: {data['country']}
🏙 المدينة: {data['city']}
📡 المزود: {data['isp']}"""
        )

    except Exception as e:
        print("ERROR:", e)
        await message.answer(f"❌ {e}")


@dp.message(Command("geo"))
async def geo_lookup(message: Message):
    print("GEO command received:", message.text)

    args = message.text.split()

    if len(args) < 2:
        await message.answer("الاستخدام:\n/geo 8.8.8.8")
        return

    ip = args[1]

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://ip-api.com/json/{ip}") as response:
                data = await response.json()

        if data.get("status") != "success":
            await message.answer("❌ لم يتم العثور على الموقع.")
            return

        lat = data["lat"]
        lon = data["lon"]

        maps = f"https://maps.google.com/?q={lat},{lon}"

        await message.answer(
            f"""📍 الموقع الجغرافي

🌍 IP: {data['query']}
🏳 الدولة: {data['country']}
📌 المنطقة: {data['regionName']}
🏙 المدينة: {data['city']}
📡 المزود: {data['isp']}

📍 الإحداثيات:
{lat}, {lon}

🗺 Google Maps:
{maps}"""
        )

    except Exception as e:
        print("ERROR:", e)
        await message.answer(f"❌ {e}")


async def main():
    print("🚀 Starting bot...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
