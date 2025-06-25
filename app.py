# app.py

import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

# Load data from database
@st.cache_data
def load_data():
    conn = sqlite3.connect("weather.db")
    query = '''
        SELECT w.temperature, w.wind_speed, r.rain
        FROM weather_data w
        JOIN rain_labels r ON w.id = r.weather_id
    '''
    df = pd.read_sql_query(query, conn)
    conn.close()
    df['wind_speed'] = df['wind_speed'].apply(lambda x: int(str(x).split()[0]) if x else 0)
    return df.dropna()

# Load data
df = load_data()

st.title("Rain Prediction Dashboard")

# Section 1: Data Preview
st.subheader("Forecast Data")
st.dataframe(df.head())

# Section 2: EDA
st.subheader("Exploratory Data Analysis")

col1, col2 = st.columns(2)

with col1:
    st.write("**Temperature Distribution**")
    fig1, ax1 = plt.subplots()
    df['temperature'].hist(ax=ax1, bins=10)
    st.pyplot(fig1)

with col2:
    st.write("**Wind Speed Distribution**")
    fig2, ax2 = plt.subplots()
    df['wind_speed'].hist(ax=ax2, bins=10, color='orange')
    st.pyplot(fig2)

st.write("**Rain Class Count**")
fig3, ax3 = plt.subplots()
df['rain'].value_counts().plot(kind='bar', ax=ax3, color=['skyblue', 'gray'])
ax3.set_xticks([0, 1])
ax3.set_xticklabels(['No Rain', 'Rain'])
st.pyplot(fig3)

# Section 3: Predict New Input (optional)
st.subheader("Try Your Own Prediction")

temp_input = st.slider("Temperature (°F)", min_value=0, max_value=120, value=70)
wind_input = st.slider("Wind Speed (mph)", min_value=0, max_value=50, value=10)

# Train model on full data
X = df[['temperature', 'wind_speed']]
y = df['rain']
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

user_input = pd.DataFrame([[temp_input, wind_input]], columns=['temperature', 'wind_speed'])
prediction = model.predict(user_input)[0]

st.write("### Prediction:")
st.success("Rain Expected " if prediction == 1 else "No Rain ")

