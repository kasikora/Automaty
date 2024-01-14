import random

import numpy

numpy.set_printoptions(linewidth=256)


class Road:
    def __init__(self):
        self.has_car = 0
        self.had_car = 0
        self.ahead = None
        self.left = None
        self.right = None
        self.neighbours = []
        self.next_neighbour = None
        self.just_follow_the_orders = []

    def clear_neighbour_list(self):
        self.neighbours = []

    def update_neighbour_list(self):
        if self.ahead is not None:
            self.neighbours.append(self.ahead)
        if self.left is not None:
            self.neighbours.append(self.left)
        if self.right is not None:
            self.neighbours.append(self.right)

    def set_next_neighbour(self):
        if self.just_follow_the_orders:
            self.next_neighbour = self.just_follow_the_orders.pop(0)
        else:
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
                    self.next_neighbour.just_follow_the_orders = self.just_follow_the_orders
                    return self.next_neighbour
        except:
            self.has_car = 0


# class CrossRoads:
#     def __init__(self):
#         self.roads = []


class OmniPresentCrossroad:  # robienie tras w skrzyzowaniiach musza juz istniec odpowiednie somsiedztwa + rozdawanie tras
    def __init__(self):
        self.all_entrance = []  # obiekty klasy road
        self.all_exit = []
        self.paths = []

    def add_entrance(self, entrence):
        self.all_entrance.append(entrence)

    def add_exit(self, exit):
        self.all_exit.append(exit)

    def function(self, current_path):  # todo nazwac to jakos i przetestowac
        new_path = []
        for next_node in current_path[-1].neighbours:
            if next_node in current_path:
                return None
            new_path = current_path.copy
            new_path.append(next_node)
            if next_node in self.all_exit:
                self.paths.append(new_path)
                return None
            self.function(new_path)

    def create_paths(self):
        for entrance in self.all_entrance:
            self.function(entrance)

    def give_orders(self):
        for entrance in self.all_entrance:
            if entrance.has_car:
                path = random.choice(self.paths)
                path.pop(0)
                entrance.just_follow_the_orders = path

    # def wath_entrance(self):
    #     for entrance in self.all_entrance:


N = 20


# matrix = numpy.empty((N, N), dtype=Road)
# for i in range(N):
#     for j in range(N):
#         matrix[i, j] = Road()
# cars = []
# for j in range(N - 1):
#     matrix[0, j].ahead = matrix[0, j + 1]
# for j in range(N - 1):
#     matrix[j, 3].ahead = matrix[j + 1, 3]
# matrix[0, 3].right = matrix[0, 4]

# matrix[0, 0].has_car = 1
# cars.append(matrix[0, 0])
# matrix[0, 1].has_car = 1
# cars.append(matrix[0, 1])
# matrix[0, 2].has_car = 1
# cars.append(matrix[0, 2])

# print("\n", matrix)
# for i in range(N):
#     for j in range(N):
#         matrix[i, j].update_neighbour_list()

class spawner:
    def __init__(self, spawnpoint, frequency):
        self.spawnpoint = spawnpoint
        self.frequency = frequency


matrix = numpy.empty((N, N), dtype=Road)

for i in range(N - 1):
    matrix[i, 10].neighbours.append(matrix[i + 1, 10])
for i in range(N - 1):
    matrix[i + 1, 10].neighbours.append(matrix[i, 10])

for i in range(N - 1):
    matrix[10, i].neighbours.append(matrix[10, i + 1])
for i in range(N - 1):
    matrix[10, i + 1].neighbours.append(matrix[10, i])
#
# crossA = OmniPresentCrossroad
#
# for i in cars:
#     i.set_next_neighbour()
#
#
# def cars_go(cars):
#     new_cars = []
#     while len(cars):
#         ten = random.randint(0, len(cars) - 1)
#
#         new_cars.append(cars[ten].drive())
#         if new_cars[-1] is None:
#             new_cars.pop(-1)
#         cars.pop(ten)
#     return new_cars
#
#
# for i in range(4):
#     cars = cars_go(cars)
#     print("\n", matrix)
#
# a = [Road(), Road(), Road()]
# a[0].ahead = a[1]
# a[1].ahead = a[2]
# a[2].ahead = a[0]
# a[0].has_car = 1
#
# print(a)
# for i in a:
#     print(a)
#     i.drive()
# print(a)
