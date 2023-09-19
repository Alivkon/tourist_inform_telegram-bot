
from key import API_TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

from forbidden_words import forb_Words
bot = Bot(token="6428551459:AAFiF11jto9T65dlf8Y5MtkVZjzksVoX5Ko") #key Kapybar
from key import API_TOKEN
#bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

async def forbidden_msg(message: types.Message):
    for word in forb_Words:
       # if word in forb_Words:
        if word in message.text:
           print("Есть такое слово")  
           await forward_message_to_admin(message)
           

async def forward_message_to_admin(message: types.Message):
    # Пересылаем сообщение администратору
    print("message.message_id = ",message.message_id)
  #  await bot.forward_message(chat_id=1232578036, from_chat_id=message.chat.id, message_id=message.message_id)
    # Создаем кнопку "Удалить" для сообщения
    keyboard = types.InlineKeyboardMarkup()
    delete_button = types.InlineKeyboardButton(text="Удалить", callback_data=f"delete_{message.message_id}_{message.chat.id}")
    keyboard.add(delete_button)
    # Отправляем сообщение с кнопкой "Удалить" 
    await bot.send_message(1232578036, text= message.text, reply_markup=keyboard) # Александр программист
    #await bot.send_message(
    #    5808424974, text=message.text, reply_markup=keyboard
    #)  # Александр test
    await bot.send_message(
        1967673032, text=message.text, reply_markup=keyboard
    )  # Сергей owner
    print("Отправляем сообщение с кнопкой 'Удалить'")
    print("message.chat.id =", message.chat.id)
    print("message.message_id = ", message.message_id)
   

