# etl.py

import sqlite3
from fetch_weather import get_weather_forecast

# Step 1: Fetch the weather data
df = get_weather_forecast()

# Step 2: Connect to SQLite
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

# Step 3: Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        temperature INTEGER,
        wind_speed TEXT,
        short_forecast TEXT,
        detailed_forecast TEXT
    )
''')

# Step 4: Insert data into the table
for _, row in df.iterrows():
    cursor.execute('''
        INSERT INTO weather_data (timestamp, temperature, wind_speed, short_forecast, detailed_forecast)
        VALUES (?, ?, ?, ?, ?)
    ''', (row['startTime'], row['temperature'], row['windSpeed'], row['shortForecast'], row['detailedForecast']))

conn.commit()
conn.close()

print(" Weather data saved to weather.db")
