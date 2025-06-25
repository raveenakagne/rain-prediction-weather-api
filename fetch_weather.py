# fetch_weather.py
import requests
import pandas as pd

def get_weather_forecast():
    url = "https://api.weather.gov/gridpoints/OKX/33,35/forecast"
    response = requests.get(url)
    data = response.json()
    periods = data['properties']['periods']
    
    df = pd.DataFrame(periods)
    df = df[['startTime', 'temperature', 'windSpeed', 'shortForecast', 'detailedForecast']]
    return df
