import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def nearest_neighbour(cities, start_city):
    unvisited = list(cities.keys())
    route = [start_city]

    current_city = start_city
    unvisited.remove(start_city)

    total_distance = 0

    while unvisited:
        nearest_city = None
        nearest_distance = float("inf")

        for city in unvisited:
            distance = calculate_distance(
                cities[current_city],
                cities[city]
            )

            if distance < nearest_distance:
                nearest_distance = distance
                nearest_city = city

        route.append(nearest_city)
        total_distance += nearest_distance

        current_city = nearest_city
        unvisited.remove(nearest_city)

    # Return to starting city
    total_distance += calculate_distance(
        cities[current_city],
        cities[start_city]
    )

    route.append(start_city)

    return route, total_distance