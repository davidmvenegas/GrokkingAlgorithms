def greedy_travel(cities, total_days):
    # Sort cities based on ratio of "coolness" to "days_required"
    cities.sort(key=lambda city: city[1] / city[2], reverse=True)

    used_days = 0
    selected_cities = []

    for city, coolness, days in cities:
        if used_days + days <= total_days:
            selected_cities.append((city, coolness, days))
            used_days += days

    return selected_cities


# Total days available for travel
DAYS_AVAILABLE = 20

# List of cities with their coolness (1-10) and days required to visit
cities = [
    ("Paris", 10, 2),
    ("Lisbon", 2, 10),
    ("Madrid", 7, 5),
    ("Dublin", 1, 11),
    ("Rome", 6, 6),
    ("Prague", 3, 9),
    ("Amsterdam", 5, 7),
    ("Berlin", 8, 3),
    ("Vienna", 4, 8),
    ("London", 9, 4),
]

itinerary = greedy_travel(cities, DAYS_AVAILABLE)

for city in itinerary:
    print(f"Visit {city[0]} for {city[2]} days. Coolness: {city[1]}")

"""
Output:
    Visit Paris for 2 days. Coolness: 10
    Visit Berlin for 3 days. Coolness: 8
    Visit London for 4 days. Coolness: 9
    Visit Madrid for 5 days. Coolness: 7
    Visit Rome for 6 days. Coolness: 6
"""
