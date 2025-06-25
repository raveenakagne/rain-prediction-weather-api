# rule_logic.py

import sqlite3

# Step 1: Connect to the database
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

# Step 2: Create new table for rain labels
cursor.execute('''
    CREATE TABLE IF NOT EXISTS rain_labels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        weather_id INTEGER,
        rain INTEGER,
        FOREIGN KEY (weather_id) REFERENCES weather_data(id)
    )
''')

# Step 3: Get all forecasts
cursor.execute("SELECT id, short_forecast, detailed_forecast FROM weather_data")
rows = cursor.fetchall()

# Step 4: Apply rule: rain = 1 if "rain" is found in forecast text
def contains_rain(*texts):
    return 1 if any("rain" in (text or "").lower() for text in texts) else 0

# Step 5: Insert into rain_labels
for row in rows:
    weather_id, short_forecast, detailed_forecast = row
    rain = contains_rain(short_forecast, detailed_forecast)
    cursor.execute('''
        INSERT INTO rain_labels (weather_id, rain)
        VALUES (?, ?)
    ''', (weather_id, rain))

conn.commit()
conn.close()

print(" Rain labels stored in table: rain_labels")
