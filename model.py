# model.py

import sqlite3
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Step 1: Load data from SQLite (join weather + labels)
conn = sqlite3.connect("weather.db")
query = '''
    SELECT w.temperature, w.wind_speed, r.rain
    FROM weather_data w
    JOIN rain_labels r ON w.id = r.weather_id
'''
df = pd.read_sql_query(query, conn)
conn.close()

# Step 2: Clean and preprocess data
def extract_wind_speed(speed):
    try:
        return int(speed.split()[0])  # Convert "15 mph" to 15
    except:
        return 0

df['wind_speed'] = df['wind_speed'].apply(extract_wind_speed)
df = df.dropna()

# Step 3: Define features and target
X = df[['temperature', 'wind_speed']]
y = df['rain']

# Step 4: Print full dataset label distribution
print("\nLabel distribution in full dataset:")
print(y.value_counts())

# Step 5: Train/test split with stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 6: Print label distribution in test set
print("\nLabel distribution in test set:")
print(y_test.value_counts())

# Step 7: Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 8: Predict and evaluate
y_pred = model.predict(X_test)
print("\n Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Step 9: Feature importance
print("\n Feature Importance:")
for feature, importance in zip(X.columns, model.feature_importances_):
    print(f"{feature}: {importance:.2f}")
