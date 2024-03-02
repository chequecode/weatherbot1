import requests
from aiogram import Bot, Dispatcher, executor, types
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Напишите свой город')


@dp.message_handler()
async def weather_data(message: types.Message):
    city_name = message.text

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={config.OPENWEATHERMAP_API_KEY}&units=metric&lang=ru'

    try:
        response = requests.get(url)

        data = response.json()

        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        pressure = data['main']['pressure']

        weather_message = f'Сейчас в городе {city_name}: \n\n' \
                          f'Описание погоды: {weather_description} \n\n' \
                          f'Температура: {temperature} \n\n' \
                          f'Ощущается как: {feels_like} \n\n' \
                          f'Влажность: {humidity} \n\n' \
                          f'Скорость ветра: {wind} \n\n' \
                          f'Давление: {pressure} \n\n' \

        await message.reply(weather_message)

    except Exception as ex:
        await message.reply('Что-то пошло не так')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)