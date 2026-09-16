# 🚗 Used Car Price Prediction

A machine learning project that estimates the resale price of a used car from its age, usage, fuel type, ownership history and condition rating. The trained model is served through an interactive Streamlit web app.

---

## Overview

Pricing a second-hand car is usually guesswork. This project turns it into a data problem: a Linear Regression model is trained on ~2,200 listings of Indian used cars, then wrapped in a simple web interface where anyone can enter a car's details and get an instant price estimate.

The repository contains the full workflow — data cleaning, encoding, model training, evaluation, serialization, and deployment.

---

## Features

- Exploratory analysis and cleaning of a real used-car listings dataset
- Label encoding of categorical fields (fuel type, ownership)
- Linear Regression model trained with an 80/20 train-test split
- Model persisted with `pickle` for reuse without retraining
- Streamlit web app with form inputs and instant prediction
- Report assets (data flow diagram, UI screenshots, results table) included

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3 |
| Data handling | Pandas, NumPy |
| Visualization | Matplotlib |
| Machine learning | Scikit-learn (LinearRegression, LabelEncoder, train_test_split) |
| Web app | Streamlit |
| Model storage | Pickle |
| Notebook | Jupyter |

---

## Project Structure

```
Used-Car-Prediciton/
├── Used_car_Prediction.ipynb   # Data cleaning, EDA, training, evaluation
├── deploy.py                   # Streamlit web application
├── car_data.csv                # Dataset (2,237 listings)
├── used_car_model.pkl          # Trained Linear Regression model
├── requirements.txt            # Python dependencies
├── Report Data/                # Diagrams and screenshots for the report
└── README.md
```

---

## Dataset

`car_data.csv` holds 2,237 used-car listings with 9 columns.

| Column | Description |
|---|---|
| Model | Car model name (434 unique values) |
| Selling Price | Resale price in ₹ — **target variable** |
| Kilometers Driven | Total distance driven |
| Year | Manufacturing year (2006–2020) |
| Owner | First / Second / Third Owner |
| Fuel Type | Diesel, Petrol, Petrol + CNG, Petrol + LPG |
| Transmission | Transmission details |
| Insurance | Insurance status or expiry date |
| Car Condition | Condition rating from 3.0 to 5.0 |

**Preprocessing steps**

1. Dropped 14 rows with missing `Insurance` values → 2,223 usable records
2. Applied `LabelEncoder` to `Fuel Type` and `Owner`
3. Selected five predictors: `Kilometers Driven`, `Year`, `Owner`, `Fuel Type`, `Car Condition`
4. Split 80% train (1,778 rows) / 20% test (445 rows)

`Model`, `Transmission` and `Insurance` were excluded because of high cardinality and inconsistent formatting.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/Used-Car-Prediciton.git
cd Used-Car-Prediciton

# (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

### Run the web app

```bash
streamlit run deploy.py
```

The app opens at `http://localhost:8501`. Enter the manufacturing year, kilometres driven, fuel type, condition rating and number of previous owners, then click **Predict Price**.

### Retrain the model

```bash
jupyter notebook Used_car_Prediction.ipynb
```

Run all cells to reproduce the cleaning, training and evaluation, and to regenerate `used_car_model.pkl`.

---

## Results

| Metric | Value |
|---|---|
| Algorithm | Linear Regression |
| Training samples | 1,778 |
| Test samples | 445 |
| R² score (test set) | **0.42** |

The model explains roughly 42% of the variance in resale price. That is a reasonable baseline given that only five numeric features are used — the strongest price drivers in this dataset are the car model and variant, which the current feature set leaves out.

---

## Known Limitations

Worth fixing before this goes any further — each one is a small change:

- **Fuel encoding mismatch.** The notebook's `LabelEncoder` sorts alphabetically (`Diesel=0`, `Petrol=1`, `Petrol + CNG=2`, `Petrol + LPG=3`), but `deploy.py` hardcodes `{"Petrol": 0, "Diesel": 1, "CNG": 2}`. Petrol and Diesel are swapped at inference time. Save the fitted encoders alongside the model instead of re-declaring the mapping by hand.
- **Owner range.** The app offers four options (0–3) while the training data only contains three ownership levels.
- **Condition input type.** Ratings in the data are decimals between 3.0 and 5.0, but the app accepts integers with a step of 1.
- **Units in the output.** The model predicts rupees (e.g. ~350,000), while the app labels the result "Lakhs". Either divide by 100,000 or change the label.
- **Year bounds.** The app allows years up to the current year, beyond the 2006–2020 range the model was trained on.

---

## Future Improvements

- Include `Model` / brand as a feature via one-hot or target encoding
- Compare Random Forest, Gradient Boosting and XGBoost against the linear baseline
- Add cross-validation and report MAE / RMSE alongside R²
- Build a scikit-learn `Pipeline` so preprocessing and the model are saved together
- Deploy publicly on Streamlit Community Cloud

---

## Author

**Deepak Kasaudhan**
B.Tech Computer Science and Engineering, Bundelkhand Institute of Engineering and Technology, Jhansi
