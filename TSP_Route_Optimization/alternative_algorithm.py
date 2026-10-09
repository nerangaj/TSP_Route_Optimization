import itertools

from tsp_algorithm import calculate_distance


def brute_force_tsp(cities, start_city):
    other_cities = [
        city for city in cities
        if city != start_city
    ]

    best_route = None
    best_distance = float("inf")

    for permutation in itertools.permutations(other_cities):

        route = [start_city] + list(permutation) + [start_city]

        total_distance = 0

        for i in range(len(route) - 1):
            total_distance += calculate_distance(
                cities[route[i]],
                cities[route[i + 1]]
            )

        if total_distance < best_distance:
            best_distance = total_distance
            best_route = route

    return best_route, best_distance