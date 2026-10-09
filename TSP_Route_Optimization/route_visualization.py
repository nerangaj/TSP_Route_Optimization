import matplotlib.pyplot as plt

from tsp_algorithm import nearest_neighbour


cities = {
    "A": (0, 0),
    "B": (2, 4),
    "C": (5, 2),
    "D": (6, 6),
    "E": (8, 3)
}


route, distance = nearest_neighbour(cities, "A")


# Get X and Y coordinates in route order
x_values = []
y_values = []

for city in route:
    x, y = cities[city]

    x_values.append(x)
    y_values.append(y)


# Draw route
plt.plot(
    x_values,
    y_values,
    marker="o"
)


# Add city labels
for city, (x, y) in cities.items():
    plt.text(
        x + 0.1,
        y + 0.1,
        city
    )


plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")

plt.title(
    f"TSP Route Using Nearest Neighbour\n"
    f"Total Distance: {distance:.2f}"
)

plt.grid(True)

plt.savefig(
    "graphs/tsp_route.png"
)

plt.show()


print("Route:", " -> ".join(route))
print(f"Total Distance: {distance:.2f}")