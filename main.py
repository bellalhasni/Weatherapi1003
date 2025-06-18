from fastapi import FastAPI
from datetime import datetime
from dotenv import load_dotenv
import requests
import uvicorn
load_dotenv()

app = FastAPI()

CITY = "DOUALA"
API_KEY = "d38e235b444ea0620814c70cbaa1be88"

def get_weather():
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(weather_url)
        data = response.json()

        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    except Exception as e:
        weather = {
            'city': 'Unknown',
            'temperature': 'N/A',
            'description': 'Unable to get data'
        }
    return weather

@app.get("/info")
async def get_info():
    weather = get_weather()

    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%M-%D")
    formatted_time = current_datetime.strftime("%H-%M-%S")

    return{
        "date":formatted_date,
        "time":formatted_time,
        "weather":weather
    }