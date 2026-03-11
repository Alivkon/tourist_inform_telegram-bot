
import datetime
import requests

response = requests.get(f"https://api.waqi.info/feed/@1849/?token=api-token")
data = response.json()
#print("ответ сервера = \n", data)
aqi = data ["data"]["aqi"]

if aqi >= 0 and aqi <= 50:
    index_aqi = "Хорошее☺️"
elif aqi > 50 and aqi <= 100:
    index_aqi = "Удовлетворительное😑"
elif aqi > 100 and aqi <= 150:
    index_aqi = "Опасное для чувствительных групп😔"
elif aqi > 150 and aqi <= 200:
    index_aqi = "Нездоровое😨"
elif aqi > 200 and aqi <= 300:
    index_aqi = "Очень нездоровое😨"  
elif aqi > 300:
    index_aqi = "Опасное🥵"       
else:
    index_aqi = "Расскажу вам попозже"

sagryaz = (f"⚠️ Качество воздуха - {index_aqi} " )

#print(sagryaz)

response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=pattaya&lang=ru&units=metric&appid=api-token")
data = response.json()
#print(data)
city = data["name"]
cur_temp = data["main"]["temp"]
feels_like= data["main"]["feels_like"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]
wind = data["wind"]["speed"]
visibility = data["visibility"]
sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
sunsrise_hour_minute = sunrise_timestamp.strftime("%H:%M")
sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
sunset_hour_minute = sunset_timestamp.strftime("%H:%M")
length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
#
pogoda=(f"🌡️Температура: { cur_temp}°C, ощущается как {feels_like}\n"
f"💧Влажность: {humidity}%\n🌬️Ветер: {wind} м/с \n"
f"🌅Восход солнца: {sunsrise_hour_minute}\n🌄Закат солнца: {sunset_hour_minute}\n➡️Продолжительность дня⬅️: {length_of_the_day}")

#print(pogoda)
