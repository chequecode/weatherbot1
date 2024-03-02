import requests
from datetime import datetime

import config


def get_monthly_forecast(city):
    params = {
        'q': city,
        'appid': config.OPENWEATHERMAP_API_KEY,
        'units': 'metric'
    }

    response = requests.get(config.BASE_URL, params=params)
    data = response.json()

    forecasts = []

    for forecast in data['list']:
        date = datetime.fromtimestamp(forecast['dt'])
        date_str = date.strftime('%Y-%m-%d')

        temperature = forecast['main']['temp']

        forecasts.append({'date': date_str, 'temp': temperature})

    return forecasts
