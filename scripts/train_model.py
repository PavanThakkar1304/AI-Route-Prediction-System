import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv("data/trips.csv")

# Create simple feature
df["stop_count"] = 1

# Features
X = df[["visit_duration", "stop_count"]]

# Target
y = df["visit_duration"] * 1.5

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor()

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model/route_model.pkl")

print("Model trained and saved successfully!")