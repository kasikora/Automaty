import random

import numpy

numpy.set_printoptions(linewidth=256)

N = 30


class Road:
    def __init__(self):
        self.has_car = 0
        self.next_hop = None

    def __str__(self):
        return f"{self.has_car}"

    def __repr__(self):
        return f"{self.has_car}"

    def drive(self):
        print(self.has_car)
        try:
            if self.has_car:
                if self.next_hop.has_car:
                    return self
                else:
                    print(":D")
                    self.next_hop.has_car = 1
                    self.has_car = 0
                    return self.next_hop
        except:
            self.has_car = 0


matrix = numpy.empty((N, N), dtype=Road)
for i in range(N):
    for j in range(N):
        matrix[i, j] = Road()
cars = []
for j in range(N - 1):
    matrix[0, j].next_hop = matrix[0, j + 1]
matrix[0, 0].has_car = 1
cars.append(matrix[0, 0])
matrix[0, 1].has_car = 1
cars.append(matrix[0, 1])

print("\n", matrix)


def cars_go(cars):
    new_cars = []
    while len(cars):
        ten = random.randint(0, len(cars) - 1)
        new_cars.append(cars[ten].drive())
        if new_cars[-1] is None:
            new_cars.pop(-1)
        cars.pop(ten)
    return new_cars


for i in range(40):
    cars = cars_go(cars)
    print("\n", matrix)

a = [Road(), Road(), Road()]
a[0].next_hop = a[1]
a[0].has_car = 1
print(a)
for i in a:
    print(a)
    i.drive()
print(a)
