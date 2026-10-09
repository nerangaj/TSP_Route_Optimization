import random
import time
import csv
import os

from tsp_algorithm import nearest_neighbour


def generate_cities(number_of_cities):
    cities = {}

    for i in range(number_of_cities):
        city_name = f"C{i + 1}"
        x = random.randint(0, 100)
        y = random.randint(0, 100)

        cities[city_name] = (x, y)

    return cities


test_sizes = [5, 10, 20, 50, 100]

results = []

print("TSP Nearest Neighbour Performance Test")
print("--------------------------------------")

for size in test_sizes:
    cities = generate_cities(size)

    start_city = "C1"

    start_time = time.perf_counter()

    route, distance = nearest_neighbour(
        cities,
        start_city
    )

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    results.append([
        size,
        round(distance, 2),
        execution_time
    ])

    print(f"\nNumber of Cities: {size}")
    print(f"Total Distance: {distance:.2f}")
    print(f"Execution Time: {execution_time:.6f} seconds")


# Create results folder
os.makedirs("results", exist_ok=True)

# Save results to CSV
with open("results/results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Number of Cities",
        "Total Distance",
        "Execution Time"
    ])

    writer.writerows(results)


print("\nResults saved to results/results.csv")