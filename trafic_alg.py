import random

import numpy

numpy.set_printoptions(linewidth=256)


class Road:
    def __init__(self, i=None, j=None):
        self.has_car = 0

        self.neighbours = []

        self.just_follow_the_orders = []
        self.from_entrance = None
        self.stop = False
        self.cords = [i, j]

        self.ahead = None
        self.left = None
        self.right = None
        self.next_neighbour = None

    def clear_neighbour_list(self):
        self.neighbours = []

    def update_neighbour_list(self):
        if self.ahead is not None:
            self.neighbours.append(self.ahead)
        if self.left is not None:
            self.neighbours.append(self.left)
        if self.right is not None:
            self.neighbours.append(self.right)

    def __str__(self):
        return f"{self.has_car}"

    def __repr__(self):
        return f"{self.has_car}"

    def set_next_neighbour(self, neighbour=None):  # todo rozdnielic moze na 2
        if neighbour is None:
            if self.neighbours:
                self.next_neighbour = random.choice(self.neighbours)
                # print(self.next_neighbour, "qweqwe")
            else:
                print("No neighbours")
        else:
            self.next_neighbour = neighbour

    def set_next_car_path(self):
        if self.just_follow_the_orders:
            self.next_neighbour.set_next_neighbour(self.just_follow_the_orders.pop(0))
            self.next_neighbour.just_follow_the_orders = self.just_follow_the_orders.copy()
            self.just_follow_the_orders = []
        else:
            self.next_neighbour.set_next_neighbour()

    def drive(self):
        # try:
        if self.has_car:
            if self.next_neighbour is not None:
                if self.next_neighbour.has_car:
                    # print("XD")
                    return self
                else:
                    # print(":D")
                    # self.next_neighbour.set_next_neighbour()
                    self.next_neighbour.has_car = 1
                    self.has_car = 0
                    print(self.just_follow_the_orders)
                    self.set_next_car_path()
                    return self.next_neighbour
            else:
                print("Nowhere to go")
                self.has_car = 0

    def drive2(self):
        if self.has_car:
            if self.stop:
                self.stop = False
                return self
            else:
                if self.just_follow_the_orders:
                    if self.just_follow_the_orders[0].has_car:
                        return self
                    else:
                        tmp_neighbour = self.just_follow_the_orders.pop(0)
                        tmp_neighbour.has_car = 1
                        tmp_neighbour.just_follow_the_orders = self.just_follow_the_orders.copy()
                        self.just_follow_the_orders = []
                        self.has_car = 0
                        return tmp_neighbour
                else:
                    if self.neighbours:
                        if self.neighbours[0].has_car:
                            return self
                        else:
                            self.neighbours[0].has_car = 1
                            self.has_car = 0
                            return self.neighbours[0]
                    else:
                        self.has_car = 0
                        print("No Neighbours")
                        return None
        else:
            print("EC PIN ERRRROOORRRRR")

        # except:
        #     self.has_car = 0
        #     print("get bugged")


# class CrossRoads:
#     def __init__(self):
#         self.roads = []


class OmniPresentCrossroad:  # robienie tras w skrzyzowaniiach musza juz istniec odpowiednie somsiedztwa + rozdawanie tras
    def __init__(self):
        self.all_entrance = []  # obiekty klasy road
        self.all_exit = []
        self.paths = []
        self.my_roads = []

    def add_entrance(self, crossroad_entrance):
        self.all_entrance.append(crossroad_entrance)

    def add_exit(self, crossroad_exit):
        self.all_exit.append(crossroad_exit)

    def function(self, current_path):  # todo nazwac to jakos i przetestowac
        new_path = []
        for next_node in current_path[-1].neighbours:
            if next_node in current_path:
                return None
            new_path = current_path.copy()
            print("tutaj: ", new_path)
            new_path.append(next_node)
            if next_node in self.all_exit:
                self.paths.append(new_path)
                return None
            if len(new_path) > 100:
                print("Path to long  ?mising exit?")
                return None
            self.function(new_path)

    def function2(self, current_path):
        this_node = current_path[-1]
        if len(current_path) > 1:
            if this_node in current_path[:-1]:
                return None
        if this_node in self.all_exit:
            self.paths.append(current_path)
            return None
        if len(current_path) > 100:
            print("Path to long  ?mising exit?")
            return None
        for node in this_node.neighbours:
            new_path = current_path.copy()
            new_path.append(node)
            self.function2(new_path)

    def create_paths(self):
        print(self.all_entrance)
        print(self.all_exit)
        for entrance in self.all_entrance:
            tmp_path = []
            tmp_path.append(entrance)
            self.function2(tmp_path)
        print(self.paths, "\n", len(self.paths))

    def give_orders(self):
        for entrance in self.all_entrance:
            if entrance.has_car and not entrance.just_follow_the_orders:
                # path.pop(0)
                paths_for_that_entrance = []
                for path in self.paths:
                    if path[0] is entrance:
                        paths_for_that_entrance.append(path)
                path = random.choice(paths_for_that_entrance)
                entrance.just_follow_the_orders = path[1:].copy()
                # entrance.just_follow_the_orders = path[2:].copy()
                # entrance.set_next_car_path()
                # entrance.from_entrance = path[0]

    def create_my_roads(self):
        for path in self.paths:
            for node in path:
                if node not in self.my_roads:
                    self.my_roads.append(node)

    def basic_rule(self):  # todo wymyslic skad wziac kierunek sciezki
        cars = []
        for node in self.my_roads:
            if node.has_car:
                cars.append(node)
        for car1 in cars:
            for car2 in cars:
                if car1 is not car2:
                    for i in range(min(len(car1.just_follow_the_orders), len(car2.just_follow_the_orders)) - 1):
                        if car1.just_follow_the_orders[i] is car2.just_follow_the_orders[i]:
                            car1.stop = True
                        if car1.just_follow_the_orders[i] is car2.just_follow_the_orders[i + 1]:
                            car1.stop = True

    # todo samochod czeka gdzy jego sciezke przecina inny z indexem rownym lub o 1 wiekszym
    # def wath_entrance(self):
    #     for entrance in self.all_entrance:


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

class Spawner:
    def __init__(self, spawnpoint_road_object, frequency_spawn_percentage_chance=20):
        self.spawnpoint = spawnpoint_road_object
        self.frequency = frequency_spawn_percentage_chance % 99
        print(self.frequency)

    def spawn(self, car_list):
        if random.choices([0, 1], weights=[100 - self.frequency, self.frequency], k=1)[0]:
            print("Spawning new fgdfhd")
            self.spawnpoint.has_car = 1
            car_list.append(self.spawnpoint)
            # self.spawnpoint.set_next_neighbour()


class SpawnersListObject:
    def __init__(self):
        self.list_of_spawners = []

    def add_spawner(self, spawner_to_add):
        self.list_of_spawners.append(spawner_to_add)

    def spawn_all(self, car_list):
        for spawner in self.list_of_spawners:
            spawner.spawn(car_list)


def make_road_matrix(N):
    matrix = numpy.empty((N, N), dtype=Road)
    for i in range(N):
        for j in range(N):
            matrix[i, j] = Road(i, j)
    print(matrix)
    return matrix


def cars_go(cars):
    new_cars = []
    while len(cars):
        ten = random.randint(0, len(cars) - 1)
        new_cars.append(cars[ten].drive2())
        if new_cars[-1] is None:
            new_cars.pop(-1)
        cars.pop(ten)
    return new_cars
    # new_cars = []
    # random.shuffle(new_cars)
    # for car in cars:
    #     new_cars.append(car.drive())
    # return new_cars


N = 20

matrix = make_road_matrix(N)
spawners = SpawnersListObject()

for i in range(N - 1):
    matrix[i, 10].neighbours.append(matrix[i + 1, 10])
for i in range(N - 1):
    matrix[i + 1, 11].neighbours.append(matrix[i, 11])
spawners.add_spawner(Spawner(matrix[0, 10], frequency_spawn_percentage_chance=20))
# spawners.add_spawner(Spawner(matrix[N - 1, 11]))

for i in range(N - 1):
    matrix[11, i].neighbours.append(matrix[11, i + 1])
for i in range(N - 1):
    matrix[10, i + 1].neighbours.append(matrix[10, i])
# spawners.add_spawner(Spawner(matrix[11, 0]))
# spawners.add_spawner(Spawner(matrix[10, N - 1]))

cars = []
for i in spawners.list_of_spawners:
    print(i)

crossroad1 = OmniPresentCrossroad()

crossroad1.add_entrance(matrix[9, 10])
crossroad1.add_entrance(matrix[10, 12])
crossroad1.add_entrance(matrix[12, 11])
crossroad1.add_entrance(matrix[11, 9])

crossroad1.add_exit(matrix[9, 11])
crossroad1.add_exit(matrix[11, 12])
crossroad1.add_exit(matrix[12, 10])
crossroad1.add_exit(matrix[10, 9])

crossroad1.create_paths()

for i in range(30):
    spawners.spawn_all(cars)
    crossroad1.give_orders()
    print(cars)
    cars = cars_go(cars)
    print("\n", matrix)

# for i in cars:
#     i.set_next_neighbour()
#
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
