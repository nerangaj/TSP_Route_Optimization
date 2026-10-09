import csv
import matplotlib.pyplot as plt
import os


cities = []
nn_times = []
bf_times = []


with open(
    "results/algorithm_comparison.csv",
    "r"
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        cities.append(int(row["Cities"]))
        nn_times.append(float(row["NN Time"]))
        bf_times.append(float(row["Brute Force Time"]))


plt.plot(
    cities,
    nn_times,
    marker="o",
    label="Nearest Neighbour"
)

plt.plot(
    cities,
    bf_times,
    marker="o",
    label="Brute Force"
)

plt.xlabel("Number of Cities")
plt.ylabel("Execution Time (Seconds)")

plt.title(
    "Nearest Neighbour vs Brute Force"
)

plt.legend()
plt.grid(True)

os.makedirs("graphs", exist_ok=True)

plt.savefig(
    "graphs/algorithm_comparison.png"
)

plt.show()