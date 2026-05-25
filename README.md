# AI Route Prediction System

An AI-powered route optimization and travel time prediction system built using **FastAPI**, **Machine Learning**, and **Route Optimization Algorithms**.

This project predicts optimized daily routes for drivers based on historical trip data and location coordinates. It also estimates travel duration and provides confidence scores through REST APIs.

---

# 🚀 Features

* ✅ Daily Route Prediction
* ✅ Route Optimization using Nearest Neighbor Algorithm
* ✅ Machine Learning-based Travel Time Prediction
* ✅ FastAPI Backend APIs
* ✅ Swagger API Documentation
* ✅ Synthetic Dataset Generation
* ✅ Model Training & Saving
* ✅ Health Check API
* ✅ GitHub Version Control

---

# 🧠 Problem Statement

Field sales drivers often create routes manually, leading to:

* Increased travel time
* Higher fuel costs
* Missed customer visits
* Poor route efficiency

This project provides an AI-based system that:

* Learns from historical trip data
* Recommends optimized routes
* Predicts estimated travel time
* Exposes predictions through REST APIs

---

# 🛠️ Tech Stack

| Technology            | Purpose                |
| --------------------- | ---------------------- |
| Python                | Backend Development    |
| FastAPI               | REST API Framework     |
| Scikit-learn          | Machine Learning       |
| Pandas                | Data Processing        |
| RandomForestRegressor | Travel Time Prediction |
| Joblib                | Model Saving/Loading   |
| Uvicorn               | FastAPI Server         |

---

# 📁 Project Structure

```text
AI-Route-Prediction-System/
│
├── api/
├── data/
│   └── trips.csv
│
├── model/
│   └── route_model.pkl
│
├── notebooks/
│
├── scripts/
│   ├── generate_data.py
│   ├── optimizer.py
│   ├── test_optimizer.py
│   └── train_model.py
│
├── tests/
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/PavanThakkar1304/AI-Route-Prediction-System.git
```

---

## 2. Navigate to Project Folder

```bash
cd AI-Route-Prediction-System
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Start FastAPI server:

```bash
uvicorn main:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

---

# 📘 Swagger API Documentation

FastAPI automatically provides Swagger UI documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoints

| Method | Endpoint         | Description                   |
| ------ | ---------------- | ----------------------------- |
| GET    | `/`              | Home API                      |
| GET    | `/health`        | Health Check                  |
| POST   | `/predict/daily` | Predict Optimized Daily Route |

---

# 📥 Sample API Request

## POST `/predict/daily`

```json
{
  "locations": [
    {
      "store": "Store_A",
      "latitude": 23.0225,
      "longitude": 72.5714
    },
    {
      "store": "Store_B",
      "latitude": 23.0500,
      "longitude": 72.6000
    },
    {
      "store": "Store_C",
      "latitude": 23.0300,
      "longitude": 72.5800
    }
  ]
}
```

---

# 📤 Sample API Response

```json
{
  "recommended_route": [
    {
      "store": "Store_A",
      "latitude": 23.0225,
      "longitude": 72.5714
    },
    {
      "store": "Store_C",
      "latitude": 23.03,
      "longitude": 72.58
    },
    {
      "store": "Store_B",
      "latitude": 23.05,
      "longitude": 72.6
    }
  ],
  "predicted_time_hours": 0.5,
  "confidence": 0.89
}
```

---

# 🤖 Machine Learning Approach

The project uses:

# RandomForestRegressor

to predict estimated travel duration based on:

* Visit Duration
* Stop Count

The trained model is saved as:

```text
model/route_model.pkl
```

---

# 🧭 Route Optimization Logic

The project uses:

# Nearest Neighbor Algorithm

to optimize route sequence.

### Logic:

1. Start from current location
2. Find nearest next store
3. Repeat until all stores are visited

This minimizes travel distance and improves efficiency.

---

# 📊 Dataset

Synthetic dataset generated using Python.

Dataset contains:

* 1000+ trip records
* 10+ drivers
* 50+ store locations

Columns include:

* Driver ID
* Store Name
* Latitude
* Longitude
* Visit Time
* Visit Duration

---

# 🔮 Future Improvements

* Google Maps Distance Matrix API Integration
* Traffic-aware Dynamic Routing
* Weekly Route Prediction
* Route Visualization on Maps
* Real-time ETA Prediction
* Docker Deployment
* Advanced ML Models

---

# 👨‍💻 Author

**Pavan Thakkar**

GitHub:

```text
https://github.com/PavanThakkar1304
```

---

# 📄 License

This project is created for assignment and educational purposes.
