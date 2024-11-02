import requests

def get_weather(city_name):
    api_key = "your_openweather_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json() if response.status_code == 200 else None
