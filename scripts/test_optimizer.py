from optimizer import optimize_route

locations = [
    {"store": "A", "latitude": 23.0225, "longitude": 72.5714},
    {"store": "B", "latitude": 23.0500, "longitude": 72.6000},
    {"store": "C", "latitude": 23.0300, "longitude": 72.5800},
]

result = optimize_route(locations)

for loc in result:
    print(loc["store"])