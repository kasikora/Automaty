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
        if self.has_car and not self.next_hop.has_car:
            print(":D")
            self.next_hop.has_car = 1
            self.has_car = 0


matrix = numpy.empty((N, N), dtype=Road)
for i in range(N):
    for j in range(N):
        matrix[i, j] = Road()
roads = []
for j in range(N - 1):
    matrix[0, j].next_hop = matrix[0, j + 1]
    roads.append(matrix[0, j])
matrix[0, 0].has_car = 1
roads.reverse()
print("\n", matrix)
for i in range(2):
    for j in range(len(roads)):
        roads[j].drive()
    print("\n", matrix)

a = [Road(), Road(), Road()]
a[0].next_hop = a[1]
a[0].has_car = 1
print(a)
for i in a:
    print(a)
    i.drive()
print(a)
