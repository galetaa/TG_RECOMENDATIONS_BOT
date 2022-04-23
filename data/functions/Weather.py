# -----------------------------------------------------------------------------
# Файл реализующий работу с погодой.
# -----------------------------------------------------------------------------
import requests
from telegram import Message
from data.containers.config import weather_server, weather_api_key


def get_weather(message: Message):
    latitude = str(message.location.latitude)
    longitude = str(message.location.longitude)
    server = weather_server

    params = {'lat': latitude,
              'lon': longitude,
              'lang': 'ru_RU',
              'extra': 'true'}
    headers = {'X-Yandex-API-Key': weather_api_key}
    json = requests.get(server, params=params, headers=headers).json()
    weather_per_day = json['forecasts'][0]['parts']['day']
    try:
        city = json['geo_object']['locality']['name']
    except Exception:
        city = ''
    max_temp = str(weather_per_day['temp_max'])
    min_temp = str(weather_per_day['temp_min'])
    wnd_sped = str(weather_per_day['wind_speed'])
    return f'Погода на сегодня.\n\nВ городе {city} сегодня максимальная ' \
           f'температура будет составлять {max_temp}°C, самой низкой' \
           f' будет температура {min_temp}°C, средняя скорость ветра ' \
           f'- {wnd_sped} м/с.'
