from tsp_algorithm import nearest_neighbour

cities = {
    "A": (0, 0),
    "B": (2, 4),
    "C": (5, 2),
    "D": (6, 6),
    "E": (8, 3)
}

start_city = "A"

route, distance = nearest_neighbour(cities, start_city)

print("Optimized Route:")
print(" -> ".join(route))

print("\nTotal Distance:")
print(round(distance, 2))