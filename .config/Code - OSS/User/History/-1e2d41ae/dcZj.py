import os, requests
from dotenv import load_dotenv

load_dotenv()
openweather_api_key = os.getenv("OPENWEATHER_API_KEY")

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_api_key}&units=imperial"
    response = requests.get(url)
    return response.json()

weather_data = get_weather_data("85308")
print(weather_data)