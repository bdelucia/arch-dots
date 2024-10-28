import os
from dotenv import load_dotenv

load_dotenv()
openweather_api_key = os.getenv("OPENWEATHER_API_KEY")
rounded_temp = math.ceil(weather_data["temp"]) # Rounds temperature up to whole number for better presentation
