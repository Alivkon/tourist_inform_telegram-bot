

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

bot = Bot(token="api-token")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

async def mes_detail_info(message: types.Message):
    #    # Проверяем, содержит ли сообщение ключевые слова
    sndTxt = (
        "Текст: "
        + str(message.text)
        + "\nОт: "
        + str(message.from_user.first_name)
        + "\nid Пользователя: "
        + str(message.from_user.id)
        + ", \nИз группы: "
        + str(message.chat.title)
        + ", \nidГруппы: "
        + str(message.chat.id)
        + ", \nMessageID: "
        + str(message.message_id)
    )
    #await bot.forward_message(chat_id=1232578036)#, text=sndTxt)
    await bot.send_message(chat_id=1232578036, text=sndTxt)
