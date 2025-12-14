from aiogram import Bot, Dispatcher, executor, types
import json, os

# --- TOKEN VA ADMIN ---
TOKEN = "8526958701:AAG2k3j5CrDiCA8_hIMW5Wp9Jfyb7o9uWlc"
ADMIN_ID = 7856514246  # Telegram ID

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

FILE = "users.json"

# --- FUNKSIYALAR ---
def load_users():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# --- START ---
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "📘 Ona tili (Milliy serti
