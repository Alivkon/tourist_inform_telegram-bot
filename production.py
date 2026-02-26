from datetime import datetime
import math
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from mes_detail import mes_detail_info
from forbidden_def import forbidden_msg
from texts_msg import msg_11, msg_15, msg_20, msg_00
from weather_vibrosi import sagryaz,pogoda
import requests

bot = Bot(token="telegram-key Kapybar")  # key Kapybar
from key import API_TOKEN

# bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

scheduler_11 = AsyncIOScheduler()
scheduler_15 = AsyncIOScheduler()
scheduler_20 = AsyncIOScheduler()
scheduler_00 = AsyncIOScheduler()
scheduler_some = AsyncIOScheduler()
# python -m pip install apscheduler

current_dateTime = datetime.now()
print(current_dateTime.minute)
now = datetime.now()
hr = now.hour
min = now.minute + 1
print("hour= ",hr)
print("min=", min)


@scheduler_some.scheduled_job("cron", day="1-31", hour=hr, minute=min)
async def scheduled_job():
    # await message_4key()
    # await bot.pin_chat_message(chat_id=-931417996, message_id=554, disable_notification=True)
    print("Задание на первый раз")
    print("msg_11")
    await msg_11()
    print("msg_15")
    #   await msg_15()
    print("msg_20")
    #   await msg_20()
    print("msg_00")
    #  await msg_00()
    print("Задание на первый раз выполнено")
scheduler_some.start()

@scheduler_11.scheduled_job("cron", day="1-31", hour=11)
# @scheduler_10.scheduled_job('cron', day='1-31', hour='1-23',minute = '0-59')
async def scheduled_job():
    print("начало задания scheduler_11")
    await msg_11()
    print("задания scheduler_11 выполнено")
scheduler_11.start()

@scheduler_15.scheduled_job("cron", day="1-31", hour=15)
async def scheduled_job():
    await msg_15()
    print("Задание на 15 выполнено")
scheduler_15.start()


@scheduler_20.scheduled_job("cron", day="1-31", hour=20)
async def scheduled_job():
    print("msg_20")
    await msg_20()
    print("Задание на 20 выполнено")


scheduler_20.start()


@scheduler_00.scheduled_job("cron", day="1-31", hour=0)
async def scheduled_job():
    print("msg_00")
    await msg_00()
    print("Задание на 00 выполнено")


scheduler_00.start()


@dp.message_handler()
async def echo(message: types.Message):
    # Пересылаем подробное сообщение администратору
    await mes_detail_info(message)
    await forbidden_msg(message)
    # await bot.forward_message(chat_id=1232578036, from_chat_id=message.chat.id, message_id=message.message_id)
    # Создаем кнопку "Удалить" для сообщения


@dp.callback_query_handler(lambda query: query.data.startswith("delete_"))
async def delete_message(callback_query: types.CallbackQuery):
    # Извлекаем ID сообщения, которое нужно удалить
    data_parts = callback_query.data.split("_")
    message_id_to_delete = int(data_parts[1])
    #  message_id_to_delete = int(callback_query.data.split("_")[2])
    print("message_id_to_delete =", message_id_to_delete)
    chat_id_to_delete = str(data_parts[2])

    print("chat_id_to_delete =", chat_id_to_delete)
    # Удаляем сообщение из главного чата
    await bot.delete_message(chat_id=chat_id_to_delete, message_id=message_id_to_delete)
    # await bot.delete_message(chat_id=-931417996, message_id=message_id_to_delete)
    # Удаляем кнопку "Удалить" из сообщения администратора
    print("Удаляем кнопку 'Удалить' из сообщения администратора")
    print("chat_id = ", callback_query.message.chat.id)
    print("callback_query.message.message_id = ", callback_query.message.message_id)

    await bot.edit_message_reply_markup(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=None,
    )
    print("deleted")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
