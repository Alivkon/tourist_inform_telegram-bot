import arrow
import requests
import json
from datetime import datetime, timedelta

# Попытка получить данные из интернета
try:
    start = arrow.now().floor('day')
    end = arrow.now().shift(days=1).floor('day')

    response = requests.get(
        'https://api.stormglass.io/v2/tide/extremes/point',
        params={
            'lat': 12.92,
            'lng': 100.88,
            'start': start.to('UTC').timestamp(),
            'end': end.to('UTC').timestamp(),
        },
        headers={
              'Authorization': '99f0fdea-52db-11ee-8b7f-0242ac130002-99f0fea8-52db-11ee-8b7f-0242ac130002'

        }
    )

    # Проверка на успешное получение данных
    if response.status_code == 200:
        # Сохранение данных в файл
        with open("response.json", "w") as response_file:
            json.dump(response.json(), response_file)
    else:
        # Если произошла ошибка при получении данных, записываем сообщение
        prilivs = "Об этом я расскажу вам в следующий раз"
except Exception as e:
    # Если произошла какая-либо другая ошибка, также записываем сообщение
    prilivs = "Об этом я расскажу вам в следующий раз"
else:
    # Если данные получены успешно, продолжаем их обработку
    # Открываем файл и загружаем данные
    with open("response.json", "r") as json_file:
        data = json.load(json_file)
    requestCount  =  data["meta"]["requestCount"]
    print("запрос к stormglass.io № ",requestCount )
    # Получаем массив данных
    data_array = data.get("data", [])

    # Создаем словарь для замены типов
    type_mapping = {"high": "⬆️прилив", "low": "⬇️отлив"}

    # Текстовая переменная для сохранения вывода
    prilivs = ""

    # Получаем текущую дату
    current_date = datetime.now().date()

    # Переводим текущее время в регион +7 часов
    current_time_utc = datetime.utcnow()
    current_time_local = current_time_utc + timedelta(hours=7)

    for item in data_array:
        dt = datetime.fromisoformat(item.get("time", ""))
        date = dt.date()

        # Проверяем, что дата находится в сегодняшний день
        if date == current_date:
            height = item.get("height", "")
            type_ = item.get("type", "")

            # Заменяем тип на прилив или отлив
            type_ = type_mapping.get(type_, type_)

            # Переводим время в регион +7 часов
            time_utc = dt + timedelta(hours=7)
            formatted_time = time_utc.strftime("%H:%M")

            # Формируем строку вывода
            output_line = f"{formatted_time} {type_}\n"

            # Добавляем строку в текстовую переменную
            prilivs += output_line

# Выводим всю текстовую переменную
#print(prilivs)
