import random

import numpy

numpy.set_printoptions(linewidth=256)

N = 20


class Road:
    def __init__(self):
        self.has_car = 0
        self.ahead = None
        self.left = None
        self.right = None
        self.neighbours = []
        self.next_neighbour = None

    def update_neighbour_list(self):
        if self.ahead is not None:
            self.neighbours.append(self.ahead)
        if self.left is not None:
            self.neighbours.append(self.left)
        if self.right is not None:
            self.neighbours.append(self.right)

    def set_next_neighbour(self):
        self.next_neighbour = random.choice(self.neighbours)
        print(self.next_neighbour, "qweqwe")

    def __str__(self):
        return f"{self.has_car}"

    def __repr__(self):
        return f"{self.has_car}"

    def drive(self):
        # print(self.has_car)
        try:
            if self.has_car:
                if self.next_neighbour.has_car:
                    print("XD")
                    return self
                else:
                    print(":D")
                    self.next_neighbour.has_car = 1
                    self.has_car = 0
                    self.next_neighbour.set_next_neighbour()
                    return self.next_neighbour
        except:
            self.has_car = 0


matrix = numpy.empty((N, N), dtype=Road)
for i in range(N):
    for j in range(N):
        matrix[i, j] = Road()
cars = []
for j in range(N - 1):
    matrix[0, j].ahead = matrix[0, j + 1]
for j in range(N - 1):
    matrix[j, 3].ahead = matrix[j + 1, 3]
matrix[0, 3].right = matrix[0, 4]

matrix[0, 0].has_car = 1
cars.append(matrix[0, 0])
matrix[0, 1].has_car = 1
cars.append(matrix[0, 1])
matrix[0, 2].has_car = 1
cars.append(matrix[0, 2])

print("\n", matrix)
for i in range(N):
    for j in range(N):
        matrix[i, j].update_neighbour_list()

print(matrix[0, 2].neighbours)
print(matrix[0, 3].neighbours)

for i in cars:
    i.set_next_neighbour()


def cars_go(cars):
    new_cars = []
    while len(cars):
        ten = random.randint(0, len(cars) - 1)

        new_cars.append(cars[ten].drive())
        if new_cars[-1] is None:
            new_cars.pop(-1)
        cars.pop(ten)
    return new_cars


for i in range(4):
    cars = cars_go(cars)
    print("\n", matrix)

a = [Road(), Road(), Road()]
a[0].ahead = a[1]
a[1].ahead = a[2]
a[2].ahead = a[0]
a[0].has_car = 1

print(a)
for i in a:
    print(a)
    i.drive()
print(a)
