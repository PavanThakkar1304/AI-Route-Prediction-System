import pandas as pd
import random
from datetime import datetime, timedelta

# Create 10 drivers
drivers = [f"D{i}" for i in range(1, 11)]

# Create 50 stores
locations = []

base_lat = 23.0225
base_lon = 72.5714

for i in range(50):
    locations.append(
        (
            f"Store_{i+1}",
            base_lat + random.uniform(-0.1, 0.1),
            base_lon + random.uniform(-0.1, 0.1)
        )
    )

data = []

start_date = datetime(2026, 1, 1)

# Generate 1000 records
for i in range(1000):

    driver = random.choice(drivers)

    location = random.choice(locations)

    date = start_date + timedelta(days=random.randint(0, 90))

    visit_duration = random.randint(10, 40)

    visit_hour = random.randint(8, 18)

    row = {
        "driver_id": driver,
        "date": date.strftime("%Y-%m-%d"),
        "store": location[0],
        "latitude": round(location[1], 6),
        "longitude": round(location[2], 6),
        "visit_time": f"{visit_hour}:00",
        "visit_duration": visit_duration
    }

    data.append(row)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save CSV
df.to_csv("data/trips.csv", index=False)

print("Dataset generated successfully!")