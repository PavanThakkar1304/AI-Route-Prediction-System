from math import radians, sin, cos, sqrt, atan2

# Function to calculate distance between two coordinates
def calculate_distance(lat1, lon1, lat2, lon2):

    R = 6371  # Earth radius in KM

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


# Nearest Neighbor Route Optimization
def optimize_route(locations):

    if not locations:
        return []

    optimized_route = []

    current = locations[0]

    remaining = locations[1:]

    optimized_route.append(current)

    while remaining:

        nearest = min(
            remaining,
            key=lambda x: calculate_distance(
                current["latitude"],
                current["longitude"],
                x["latitude"],
                x["longitude"]
            )
        )

        optimized_route.append(nearest)

        remaining.remove(nearest)

        current = nearest

    return optimized_route