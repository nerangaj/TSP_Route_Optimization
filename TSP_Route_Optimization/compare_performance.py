import random
import time
import csv
import os

from tsp_algorithm import nearest_neighbour
from alternative_algorithm import brute_force_tsp


def generate_cities(number_of_cities):
    cities = {}

    for i in range(number_of_cities):
        city_name = f"C{i + 1}"
        x = random.randint(0, 100)
        y = random.randint(0, 100)

        cities[city_name] = (x, y)

    return cities


test_sizes = [5, 6, 7, 8, 9]

results = []

print("Algorithm Performance Comparison")
print("--------------------------------")

for size in test_sizes:

    cities = generate_cities(size)
    start_city = "C1"

    # Nearest Neighbour
    nn_start = time.perf_counter()

    nn_route, nn_distance = nearest_neighbour(
        cities,
        start_city
    )

    nn_time = time.perf_counter() - nn_start


    # Brute Force
    bf_start = time.perf_counter()

    bf_route, bf_distance = brute_force_tsp(
        cities,
        start_city
    )

    bf_time = time.perf_counter() - bf_start


    difference = nn_distance - bf_distance

    results.append([
        size,
        nn_distance,
        nn_time,
        bf_distance,
        bf_time,
        difference
    ])


    print(f"\nCities: {size}")

    print(
        f"Nearest Neighbour - "
        f"Distance: {nn_distance:.2f}, "
        f"Time: {nn_time:.8f}"
    )

    print(
        f"Brute Force - "
        f"Distance: {bf_distance:.2f}, "
        f"Time: {bf_time:.8f}"
    )


# Save CSV
os.makedirs("results", exist_ok=True)

with open(
    "results/algorithm_comparison.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Cities",
        "NN Distance",
        "NN Time",
        "Brute Force Distance",
        "Brute Force Time",
        "Distance Difference"
    ])

    writer.writerows(results)


print(
    "\nResults saved to "
    "results/algorithm_comparison.csv"
)