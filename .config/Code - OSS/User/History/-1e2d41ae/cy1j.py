import os
from dotenv import load_dotenv

load_dotenv()
openweather_api_key = os.getenv("OPENWEATHER_API_KEY")
weather_data = get_weather_data("85308")
print(weather_data)