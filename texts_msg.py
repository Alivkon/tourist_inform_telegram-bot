from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from sys import path
from weather_vibrosi import sagryaz, pogoda
# from os import path

bot = Bot(token="6428551459:AAFiF11jto9T65dlf8Y5MtkVZjzksVoX5Ko")  # key Kapybar
from key import API_TOKEN
from stormglass_extrem_tides import prilivs
# bot = Bot(token=API_TOKEN)

text_variable = "Лена про Таиланд"
group_link = "https://t.me/thaiiznutri"
formatted_text = f'<a href="{group_link}">{text_variable}</a>'

textmsg_10 = f"Ghbdtn➡️➡️ 😀0️⃣🍋 📌🍋🍋🤗🥑⬅️⬅️\n\n" f"👋<i>{formatted_text}</i> \U0001F60D"

textmsg_11 = (
    f"<b> 🎙️🦫 КАААП Паттайцы и Паттайчанки!\n\n"
    f" 🫠🧯 Погода - кайф, кстати, что там?</b>\n"
    f"{pogoda}\n\n"
    f"🌬️ <b>Давай глянем на загрязнение воздуха, хотя мне все равно.</b>\n"
    f"{sagryaz}\n\n"
    f"🌊 <b>Как там сегодня на пляже?</b>\n"
    f"{prilivs}\n"
    f"Полезная информация ⤵️\n\n"
    f' 👉👉 <a href="{"https://telegra.ph/Pravila-chata-09-05-24"}">{"ПРАВИЛА"}</a>  👈👈\n\n'
    f"😉  <b>А еще, я собрал для вас лучшие сервисы услуг в Паттайе:</b>\n\n"
    f"⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️"
)

textmsg_15 = (
    f"<b>🦦 Время кушать и обсуждать.</b> \n\n"
    f"🥱 Где были, что делали - рассказывайте!\n\n"
    f"А человеки снизу помогут вам, если возникли какие-то вопросы ⤵️\n\n"
    f' 👉👉 <a href="{"https://telegra.ph/Pravila-chata-09-05-24"}">{"ПРАВИЛА"}</a>  👈👈\n\n'
    f"<b>Админ для сотрудничества:</b>\n"
    f'<a href="{"https://t.me/tto157"}">{"Василий"}</a> \n\n'
    f"<b>Админы, если возникли вопросы в чате:</b>\n"
    f'  <a href="{"https://t.me/Jorik_Jora_Rus"}">{"Жора"}</a>\n'
    f'  <a href="{"https://t.me/chikagirls"}">{"Вика"}</a> \n\n'
    f"😉  <b>А еще, я собрал для вас лучшие сервисы услуг в Паттайе:</b>\n\n"
    f"⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️"
)

textmsg_20 = (
    f"🥳 <b>Хороший день был сегодня!</b>\n\n"
    f"Я покушал и поспал. А вы что делали весь день?\n\n"
    f"<b>Давайте обсудим, покушаем, потусим и опять ляжем спать</b>👍\n\n"
    f' 👉👉 <a href="{"https://telegra.ph/Pravila-chata-09-05-24"}">{"ПРАВИЛА"}</a>   👈👈\n\n'
    f"🦦 <b>Я собрал для вас лучшие сервисы услуг в Паттайе:</b>\n\n"
    f"⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️"
)


async def msg_11():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(
            "Обмен валют (Рубли онлайн, Usdt $)",
            url="https://t.me/SenateExchange_bot?start=start_PoaH9q17",
        )
    )
    keyboard.add(
        types.InlineKeyboardButton("ЭКСКУРСИИ", url="https://t.me/+Ehy4p1YocnI1ZTky")
    )
    keyboard.add(
        types.InlineKeyboardButton("Аренда жилья", url="https://t.me/arendathailand")
    )
    keyboard.add(
        types.InlineKeyboardButton(
            "Наши чаты и каналы", url="https://telegra.ph/Nashi-chaty-i-kanaly-09-05"
        )
    )
    video_path_11 = "video\Kapibar_11.mp4"
    await bot.send_video(
        chat_id=-1001924485346,
        video=types.InputFile(video_path_11),
        caption=textmsg_11,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )
    await bot.send_video(
        chat_id=-818653502,
        video=types.InputFile(video_path_11),
        caption=textmsg_11,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )


async def msg_15():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(
            "Обмен валют (Рубли онлайн, Usdt $)",
            url="https://t.me/SenateExchange_bot?start=start_PoaH9q17",
        )
    )
    keyboard.add(
        types.InlineKeyboardButton("ЭКСКУРСИИ", url="https://t.me/+Ehy4p1YocnI1ZTky")
    )
    keyboard.add(
        types.InlineKeyboardButton("Аренда жилья", url="https://t.me/arendathailand")
    )
    keyboard.add(
        types.InlineKeyboardButton(
            "Наши чаты и каналы", url="https://telegra.ph/Nashi-chaty-i-kanaly-09-05"
        )
    )
    video_path_15 = "video\Kapibar_15.mp4"
    await bot.send_video(
        chat_id=-1001924485346,
        video=types.InputFile(video_path_15),
        caption=textmsg_15,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )

    await bot.send_video(
        chat_id=-818653502,
        video=types.InputFile(video_path_15),
        caption=textmsg_15,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )


async def msg_20():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(
            "Обмен валют (Рубли онлайн, Usdt $)",
            url="https://t.me/SenateExchange_bot?start=start_PoaH9q17",
        )
    )
    keyboard.add(
        types.InlineKeyboardButton("ЭКСКУРСИИ", url="https://t.me/+Ehy4p1YocnI1ZTky")
    )
    keyboard.add(
        types.InlineKeyboardButton("Аренда жилья", url="https://t.me/arendathailand")
    )
    keyboard.add(
        types.InlineKeyboardButton(
            "Наши чаты и каналы", url="https://telegra.ph/Nashi-chaty-i-kanaly-09-05"
        )
    )
    video_path_20 = "video\Kapibar_20.mp4"
    await bot.send_video(
        chat_id=-1001924485346,
        video=types.InputFile(video_path_20),
        caption=textmsg_20,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )

    await bot.send_video(
        chat_id=-818653502,
        video=types.InputFile(video_path_20),
        caption=textmsg_20,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )


async def msg_00():
    video_path_00 = "video\Kapibar_00.mp4"
    await bot.send_video(
        chat_id=-1001924485346,
        video=types.InputFile(video_path_00),
        disable_notification=True,
    )

    await bot.send_video(
        chat_id=-818653502,
        video=types.InputFile(video_path_00),
        disable_notification=True,
    )
