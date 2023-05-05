import openai
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config as con
from aiogram.types import User

    
openai.api_key = con.Open_ai

bot = Bot(token=con.Bot_telegram_token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

async def generate_text(prompt):
    
    completions = openai.Completion.create(
        engine=con.Engin,
        prompt=prompt+con.Prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    message = completions.choices[0].text
    return message

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_id,"Привіт! чат бот який поговорить з вами")

@dp.message_handler(content_types=['text'])
async def echo_download_message(message: types.Message):
    prompt = message.text
    text = await generate_text(prompt)
    await bot.send_message(message.from_id,text)
    print(prompt+con.Prompt)
    

if __name__ == "__main__":
    print("Да востанут машини...")
    asyncio.run(dp.start_polling())
    