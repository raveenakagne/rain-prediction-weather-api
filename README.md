# Rain Prediction Using U.S. Weather API — End-to-End Machine Learning Project

This is a complete data science project that scrapes U.S. weather forecast data from a public API, stores it in a SQLite database, labels it using rule-based logic, trains a machine learning model to predict rain, and provides an interactive dashboard for EDA and prediction.

## Features

- Scrape live weather forecast using API
- Store structured data in a relational database (SQLite)
- Apply rule-based labeling (rain = 1 if forecast mentions "rain")
- Clean and transform input data
- Train and evaluate a machine learning model (Random Forest)
- Interactive EDA and live prediction using Streamlit

## Technologies Used

| Task                | Tools & Libraries                        |
|---------------------|------------------------------------------|
| Programming         | Python 3.13                              |
| API Fetching        | `requests` + `api.weather.gov`           |
| Data Handling       | `pandas`, `matplotlib`                   |
| Storage             | `sqlite3` (local DB)                     |
| Rule Logic + Cleaning | Custom Python logic (`cleaning.py`)   |
| Machine Learning    | `scikit-learn` (RandomForestClassifier)  |
| Visualization + UI  | `Streamlit`                              |
| Version Control     | `Git`, `GitHub`                          |

## Project Structure

rain-prediction-weather-api/
│
├── fetch_weather.py # Scrape weather API and create dataframe
├── etl.py # Save structured data to SQLite
├── rule_logic.py # Apply binary label (rain = 1 if 'rain' in forecast)
├── cleaning.py # Clean & transform raw weather data
├── model.py # Train & evaluate ML model (Random Forest)
├── app.py # Streamlit dashboard for EDA and live prediction
├── weather.db # SQLite database (ignored in Git)
├── .gitignore # Ignore .db and other sensitive files
└── README.md # Project documentation

shell
Copy
Edit

## End-to-End Pipeline

### Step 1: Fetch Forecast Data
```bash
python fetch_weather.py
Step 2: Store Data in SQLite
bash
Copy
Edit
python etl.py
Step 3: Apply Rule-Based Labeling
bash
Copy
Edit
python rule_logic.py
Step 4: Clean & Prepare Data for Modeling
temperature is converted to numeric

wind_speed is extracted from text

Missing values are handled

Step 5: Train and Evaluate Model
bash
Copy
Edit
python model.py
Model: RandomForestClassifier
Features: temperature, wind_speed
Target: rain (1 = yes, 0 = no)
Evaluation: classification report, feature importance

Streamlit Dashboard
Launch the App
bash
Copy
Edit
streamlit run app.py
Dashboard Features
Preview of stored forecast data

EDA visualizations (temperature, wind, rain counts)

Live prediction form: input temperature and wind to predict rain

Cleaning Pipeline (cleaning.py)
This module:

Converts wind speed from text to integer

Handles missing or malformed values

Standardizes data for use in modeling and dashboard

Used across:

model.py

app.py

API Reference
Data Source: https://api.weather.gov
This is a free public weather API that requires no login or API key.

Sample Output
yaml
Copy
Edit
Classification Report:
              precision    recall  f1-score   support
           0       0.89      1.00      0.94         8
           1       1.00      0.80      0.89         5

Feature Importance:
temperature: 0.68
wind_speed: 0.32
To Do
 Add multi-location support

 Export data to Google BigQuery

 Automate data updates (e.g., cron job)

 Deploy Streamlit app to web/cloud

Author
Raveena Kagne
Email: raveena.kagne@gmail.com
GitHub: github.com/raveenakagne
