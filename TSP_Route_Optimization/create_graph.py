import csv
import matplotlib.pyplot as plt
import os


city_counts = []
execution_times = []


with open("results/results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        city_counts.append(
            int(row["Number of Cities"])
        )

        execution_times.append(
            float(row["Execution Time"])
        )


plt.plot(
    city_counts,
    execution_times,
    marker="o"
)

plt.xlabel("Number of Cities")
plt.ylabel("Execution Time (Seconds)")
plt.title(
    "Nearest Neighbour Algorithm Performance"
)

plt.grid(True)

os.makedirs("graphs", exist_ok=True)

plt.savefig(
    "graphs/execution_time_graph.png"
)

plt.show()