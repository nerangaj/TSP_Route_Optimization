import time

from tsp_algorithm import nearest_neighbour
from alternative_algorithm import brute_force_tsp


cities = {
    "A": (0, 0),
    "B": (2, 4),
    "C": (5, 2),
    "D": (6, 6),
    "E": (8, 3)
}


# Nearest Neighbour
start_time = time.perf_counter()

nn_route, nn_distance = nearest_neighbour(
    cities,
    "A"
)

nn_time = time.perf_counter() - start_time


# Brute Force
start_time = time.perf_counter()

bf_route, bf_distance = brute_force_tsp(
    cities,
    "A"
)

bf_time = time.perf_counter() - start_time


print("Nearest Neighbour")
print("-----------------")
print("Route:", " -> ".join(nn_route))
print(f"Distance: {nn_distance:.2f}")
print(f"Execution Time: {nn_time:.8f} seconds")


print("\nBrute Force")
print("-----------")
print("Route:", " -> ".join(bf_route))
print(f"Distance: {bf_distance:.2f}")
print(f"Execution Time: {bf_time:.8f} seconds")


print("\nComparison")
print("----------")

difference = nn_distance - bf_distance

print(f"Distance Difference: {difference:.2f}")