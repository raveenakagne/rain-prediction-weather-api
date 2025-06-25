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

License
MIT License — free for personal or commercial use.

yaml
Copy
Edit

---

Let me know if you'd like a version with images/screenshots, or instructions for deploying the dashboard online (e.g., with Streamlit Cloud or GCP).







You said:
mention what all must be present in readme file 


ChatGPT said:
A great README.md acts as the front door to your project. Whether it's for recruiters, collaborators, or your future self, it should be clear, complete, and easy to follow.

✅ Essential Sections in a Good README.md
Here’s what must be present in a professional README.md:

1. Project Title and Description
Brief overview of what the project does and its purpose

Optional: add a short summary in one line

Example:

markdown
Copy
Edit
# Rain Prediction from Weather Forecast
A machine learning pipeline that predicts whether it will rain based on U.S. weather API data.
2. Features / Key Highlights
Bullet points listing what your project can do

Example:

markdown
Copy
Edit
- Scrapes live weather data from API
- Applies rule-based rain labeling
- Trains a machine learning model
- Visualizes predictions and EDA via Streamlit
3. Tech Stack / Technologies Used
Languages, libraries, APIs, tools used in the project

Example:

markdown
Copy
Edit
- Python, SQLite, Streamlit, scikit-learn, matplotlib
- API: api.weather.gov (no API key required)
4. Project Structure
List and explain the main files and folders in the repo

Example:

markdown
Copy
Edit
├── fetch_weather.py        # API script
├── etl.py                  # Save data to SQLite
├── model.py                # ML model
├── app.py                  # Streamlit app
5. How to Run / Usage Instructions
Step-by-step commands to run each part of your project

Install dependencies, run scripts, start the app

Example:

markdown
Copy
Edit
pip install -r requirements.txt
python fetch_weather.py
python etl.py
streamlit run app.py
6. Screenshots / Visual Output (optional but helpful)
Add visuals like model results or dashboard UI

7. API Information (if applicable)
Link to the API used

Mention if it requires authentication

8. To-Do / Roadmap (optional)
Features to add later

Things that are planned or missing

9. Author Information
Name, contact info, GitHub link

10. License
MIT / Apache / etc., depending on how you want your project shared

✅ Bonus Sections (Optional but Great)
Section	Purpose
Demo Link	Link to live app or Streamlit Cloud
Environment	Python version, OS, etc.
Contribution	How others can contribute
Known Issues	Bugs, limitations, edge cases

Would you like me to give you a README template file with all these as placeholders so you can reuse it for any project?








You said:
give me for my project and git 


ChatGPT said:
Absolutely! Below is a complete and professional README.md template customized for your project, with all the best practices applied — ready to use in your GitHub repo.

✅ Full README.md for GitHub (Rain Prediction Project)
markdown
Copy
Edit
# Rain Prediction from U.S. Weather Forecast (End-to-End ML Pipeline)

This project is an end-to-end machine learning pipeline that fetches weather forecast data from a public API, stores it in a structured SQLite database, applies rule-based labeling to detect rain, trains a classification model, and visualizes predictions through an interactive Streamlit dashboard.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Dashboard](#dashboard)
- [API Details](#api-details)
- [To Do](#to-do)
- [Author](#author)
- [License](#license)

---

## Features

- Fetch live weather forecast from a free public API (no key required)
- ETL process to save structured weather data in SQLite
- Apply rule-based logic to label forecasts with `rain = 1` or `0`
- Clean data using a custom pipeline (`cleaning.py`)
- Train a machine learning model (Random Forest)
- Evaluate using precision, recall, F1-score, and feature importance
- Interactive Streamlit dashboard for data exploration and prediction

---

## Tech Stack

| Area           | Tool / Library                     |
|----------------|------------------------------------|
| Language       | Python 3.13                        |
| Data Handling  | pandas, matplotlib                 |
| Database       | sqlite3                            |
| Machine Learning | scikit-learn                     |
| API Access     | requests, api.weather.gov          |
| Dashboard      | Streamlit                          |
| Version Control| Git, GitHub                        |

---

## Project Structure

rain-prediction-weather-api/
├── fetch_weather.py # Fetch weather forecast data from API
├── etl.py # Save data into SQLite database
├── rule_logic.py # Apply rule-based rain labeling
├── cleaning.py # Reusable cleaning and transformation logic
├── model.py # Train ML model and evaluate
├── app.py # Streamlit dashboard (EDA + prediction)
├── weather.db # SQLite database (not committed)
├── .gitignore # Ignore weather.db and pycache
├── README.md # Project documentation

yaml
Copy
Edit

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/raveenakagne/rain-prediction-weather-api.git
cd rain-prediction-weather-api
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
# or manually:
pip install pandas requests scikit-learn matplotlib streamlit
3. Run the data pipeline
bash
Copy
Edit
python fetch_weather.py     # Fetch API data
python etl.py               # Save data to SQLite
python rule_logic.py        # Label data with rain = 1/0
python model.py             # Train & evaluate ML model
Dashboard
Launch Streamlit App
bash
Copy
Edit
streamlit run app.py
Includes:
Data preview table

Temperature & wind speed distributions

Rain class count

Interactive input to predict rain (based on temp and wind)

API Details
Source: https://api.weather.gov

No login or API key required

Currently fetches forecast for a default location (can be extended)

To Do
 Add support for multiple geographic locations

 Push cleaned data to Google BigQuery

 Deploy dashboard using Streamlit Cloud or GCP

 Automate daily updates with cron or Cloud Scheduler

 Add unit tests and exception handling

Author
Raveena Kagne
Email: raveena.kagne@gmail.com
GitHub: raveenakagne