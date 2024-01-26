import random
import copy
import numpy

numpy.set_printoptions(linewidth=256)


class CrosroadListObject:
    def __init__(self):
        self.crossroads_list = []

    def add_crossroad(self, crossroad):
        self.crossroads_list.append(crossroad)

    def run_func(self):
        for crossroad in self.crossroads_list:
            crossroad.give_orders()
            crossroad.right_hand_rule()
            crossroad.unstuck.unstuck()  # wolac przed swiatlami
            crossroad.all_lights_cycle()


class Road:
    def __init__(self, i=None, j=None):
        self.has_car = 0

        self.neighbours = []

        self.just_follow_the_orders = []
        self.vectors = []
        self.priority = 0

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

    # def set_next_neighbour(self, neighbour=None):  # todo rozdnielic moze na 2
    #     if neighbour is None:
    #         if self.neighbours:
    #             self.next_neighbour = random.choice(self.neighbours)
    #             # print(self.next_neighbour, "qweqwe")
    #         else:
    #             print("No neighbours")
    #     else:
    #         self.next_neighbour = neighbour
    #
    # def set_next_car_path(self):
    #     if self.just_follow_the_orders:
    #         self.next_neighbour.set_next_neighbour(self.just_follow_the_orders.pop(0))
    #         self.next_neighbour.just_follow_the_orders = self.just_follow_the_orders.copy()
    #         self.just_follow_the_orders = []
    #     else:
    #         self.next_neighbour.set_next_neighbour()

    # def drive(self):
    #     # try:
    #     if self.has_car:
    #         if self.next_neighbour is not None:
    #             if self.next_neighbour.has_car:
    #                 # print("XD")
    #                 return self
    #             else:
    #                 # print(":D")
    #                 # self.next_neighbour.set_next_neighbour()
    #                 self.next_neighbour.has_car = 1
    #                 self.has_car = 0
    #                 print(self.just_follow_the_orders)
    #                 self.set_next_car_path()
    #                 return self.next_neighbour
    #         else:
    #             print("Nowhere to go")
    #             self.has_car = 0
    def drive(self):
        if self.has_car:
            if self.stop:
                self.stop = False
                print("stopped be magic")
                return self
            else:
                if self.just_follow_the_orders:
                    if self.just_follow_the_orders[0].has_car:
                        return self
                    else:
                        next_step = self.just_follow_the_orders.pop(0)
                        self.vectors.pop(0)
                        next_step.has_car = 1
                        next_step.just_follow_the_orders = self.just_follow_the_orders.copy()
                        next_step.vectors = self.vectors.copy()
                        next_step.priority = self.priority
                        self.just_follow_the_orders = []
                        self.vectors = []  # todo moze trzeba przywrucic
                        self.has_car = 0
                        return next_step
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
                        next_step = self.just_follow_the_orders.pop(0)
                        next_step.has_car = 1
                        next_step.just_follow_the_orders = self.just_follow_the_orders.copy()
                        # print(self.just_follow_the_orders)
                        self.just_follow_the_orders = []
                        self.has_car = 0
                        return next_step
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

        self.entrance_object_list = []
        self.paths_and_vectors = []

        self.unstuck = None

        self.lights = []

    def create_unstuck(self, matrix):
        self.unstuck = OmniPresentCrossroad.Unstuck(self.my_roads, matrix)

    def create_paths_and_vectors(self):
        for path in self.paths:
            self.paths_and_vectors.append(OmniPresentCrossroad.PathAndVector(path.copy()))
        print("created paths and vectors", self.paths_and_vectors)
        print(len(self.paths_and_vectors))

    class Unstuck:
        def __init__(self, roads, matrix):  # todo moze sie uda automatyczne wejscia i wyjscia z tego
            self.roads = roads
            self.old_roads_has_car = []
            for road in self.roads:
                self.old_roads_has_car.append(road.has_car)
            print("CREATED UNSTUCK _____________________________________________________________________________________")

            # for road in roads:
            #     if len(road.neighbours) > 1:
            #         # road.has_car = 1  # todo skasowac bo nie bedzie sie dzialac
            #         self.roads.append(road)  # to jest git
            # self.unstuck_points = []
            # for road in self.roads:
            #     for i in matrix:
            #         for j in i:
            #             if road in j.neighbours and len(j.neighbours) == 1:
            #                 # j.has_car = 1  # todo skasowac bo nie bedzie sie dzialac
            #                 self.unstuck_points.append(j)
            # print("UNSTUCK: ")
            # print(self.unstuck_points)
            # print(self.roads)

        def save_has_car_values(self):
            self.old_roads_has_car = []
            for road in self.roads:
                self.old_roads_has_car.append(road.has_car)

        def unstuck(self):
            for i in range(len(self.roads)):
                if self.roads[i].has_car != self.old_roads_has_car[i]:
                    self.save_has_car_values()
                    return
            print("unstucking")
            random.shuffle(self.roads)
            tmp_counter = 2
            for node in self.roads:
                if node.just_follow_the_orders:
                    if not node.just_follow_the_orders[0].has_car and node.has_car:
                        # if not tmp_counter: # odkomentowac zeby sie nie zapychalo shrzyzowanie
                        #     break
                        # tmp_counter = tmp_counter - 1
                        node.stop = False
            # tmp_cat_list = random.choices(self.roads, k=3)
            # for car in tmp_cat_list:
            #     car.stop = False
            # self.save_has_car_values()

            # for node in self.roads:
            #     if node.has_car != 0:
            #         return
            # print("unstucking")
            # tmp = random.choice(self.roads)
            # tmp.stop = False

    def set_influence_area_for_lights_priority(self):
        for light in self.lights:
            for path in self.paths:
                if light.road_object in path:
                    for node in path:
                        if not len(node.neighbours) > 1:
                            light.influence_area.append(node)
                            break

    def all_lights_cycle(self):
        for light in self.lights:
            light.cycle()

    def add_light(self, signalization_object):
        self.lights.append(signalization_object)

    class Signalization:
        def __init__(self, road_object, time_red=60, time_green=60, starting_state=False, cords=[None, None]):
            self.time_red = time_red
            self.time_green = time_green
            self.road_object = road_object

            self.cords = cords

            self.priority = 3
            self.influence_area = []

            self.current_state = starting_state
            if starting_state is False:
                self.iterator = 0
            else:
                self.iterator = self.time_red + 1

        def cycle(self):
            self.iterator = self.iterator + 1
            self.iterator = self.iterator % (self.time_green + self.time_red)
            if self.iterator > self.time_red:
                self.current_state = 1
                for node in self.influence_area:
                    node.priority = self.priority
            else:
                self.current_state = 0
                self.road_object.stop = True
                for node in self.influence_area:
                    node.priority = 0

    class PathAndVector:
        def __init__(self, path=[], copy=False):
            self.path = path
            self.direction_vectors = []
            self.make_direction_vectors()
            self.for_entrance = None
            if self.path:
                self.for_entrance = self.path.pop(0)
            print("path_and_vector_constructor:")
            print(self.path)
            print(self.direction_vectors)

        def pop_path(self):
            self.direction_vectors.pop(0)
            return self.path.pop(0)

        def set_path(self, path):
            self.path = path

        def set_direction_vectors(self, vectors):
            self.direction_vectors = vectors

        def set_from_entrance(self, entrance):
            self.for_entrance = entrance

        def make_direction_vectors(self):
            # list_of_cords = []
            # for i_node in self.path:
            #     for i in range(len(matrix)):
            #         for j in range(len(matrix[i])):
            #             if i_node is matrix[i, j]:
            #                 list_of_cords.append([i, j])
            # for i_node in range(len(list_of_cords) - 1):
            #     i_vector = list_of_cords[i_node + 1][0] - list_of_cords[i_node][0]
            #     j_vector = list_of_cords[i_node + 1][1] - list_of_cords[i_node][1]
            #     self.direction_vectors.append([i_vector, j_vector])
            self.direction_vectors = []
            if self.path:
                list_of_cords = []
                for node in self.path:
                    list_of_cords.append(node.cords)
                for i_node in range(len(list_of_cords) - 1):
                    i_vector = list_of_cords[i_node + 1][0] - list_of_cords[i_node][0]
                    j_vector = list_of_cords[i_node + 1][1] - list_of_cords[i_node][1]
                    self.direction_vectors.append([i_vector, j_vector])  # todo zoacz czy dziala

    class Entrance:
        def __init__(self, entrance_road):
            self.entrance_road = entrance_road
            self.paths_entr = []
            self.priority = 0

            self.paths_and_vectors = []

        def set_paths_and_vectors(self, all_paths_and_vectors):
            self.paths_and_vectors = []
            for path_and_vectors in all_paths_and_vectors:
                if path_and_vectors.for_entrance is self.entrance_road:
                    print(path_and_vectors.path)
                    self.paths_and_vectors.append(path_and_vectors)  # todo sprawdzic czy nie trzeba copy()
            print(self.paths_and_vectors)

        def set_path_and_vectors_in_car(self):
            if self.entrance_road.has_car and not self.entrance_road.just_follow_the_orders:
                chosen_one = random.choice(self.paths_and_vectors)
                self.entrance_road.just_follow_the_orders = chosen_one.path.copy()
                self.entrance_road.vectors = chosen_one.direction_vectors.copy()
                self.entrance_road.priority = self.priority

        def set_paths(self, all_paths):
            self.paths_entr = []
            for path in all_paths:
                if path[0] is self.entrance_road:
                    self.paths_entr.append(path)
            # print(self.paths_entr)

        def set_path_in_car(self):
            if self.entrance_road.has_car and not self.entrance_road.just_follow_the_orders:
                # self.entrance_road.just_follow_the_orders = random.choice(self.paths)[1:].copy()
                path = random.choice(self.paths_entr)
                self.entrance_road.just_follow_the_orders = path[1:].copy()

    def create_entrance_object_list(self):
        self.entrance_object_list = []
        for entrance in self.all_entrance:
            tmp_entrance = OmniPresentCrossroad.Entrance(entrance)
            tmp_entrance.set_paths(self.paths)
            # todo testowac
            tmp_entrance.set_paths_and_vectors(self.paths_and_vectors)
            self.entrance_object_list.append(tmp_entrance)

    def add_entrance(self, crossroad_entrance):
        self.all_entrance.append(crossroad_entrance)

    def add_exit(self, crossroad_exit):
        self.all_exit.append(crossroad_exit)

    def function(self, current_path):
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
            self.function(new_path)

    def create_paths(self):
        print(self.all_entrance)
        print(self.all_exit)
        for entrance in self.all_entrance:
            tmp_path = []
            tmp_path.append(entrance)
            self.function(tmp_path)
        print(self.paths, "\n", len(self.paths))
        # self.create_entrance_object_list()

    def remove_path(self, entrance_object, exit_object):
        print(self.paths)
        for i in range(len(self.paths)):
            if self.paths[i][0] is entrance_object and self.paths[i][-1] is exit_object:
                self.paths.pop(i)
                print(len(self.paths))
                break

    def give_orders_old(self):
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

    def give_orders(self):
        for entrance in self.entrance_object_list:
            # entrance.set_path_in_car()
            entrance.set_path_and_vectors_in_car()

    def create_my_roads(self):
        for path in self.paths:
            for node in path:
                if node not in self.my_roads:
                    self.my_roads.append(node)

    def right_hand_rule(self):
        colliding_node_dict = {}
        for car_index, road in enumerate(self.my_roads):
            if road.has_car:
                for node_index, node in enumerate(road.just_follow_the_orders):
                    if node in colliding_node_dict:
                        colliding_node_dict[node].append([car_index, node_index])
                    else:
                        colliding_node_dict[node] = [[car_index, node_index]]
        print(colliding_node_dict)
        for node in colliding_node_dict.values():  # values daje tylko nieKlucze a items daje w klucza i nieklucza
            for n1 in node:
                # if self.my_roads[n1[0]] in self.unstuck.unstuck_points:
                for n2 in node:
                    if n1 is not n2:
                        if n1[1] <= n2[1] <= n1[1] + 1 and len(self.my_roads[n1[0]].neighbours) < 2:
                            print(n1[1], n2[1])
                            a = self.my_roads[n1[0]].vectors[n1[1]]
                            b = self.my_roads[n2[0]].vectors[n2[1]]
                            c = a[1] * b[0] - a[0] * b[1]
                            print("angle", c)
                            # if c == 1:
                            #     self.my_roads[n2[0]].stop = True
                            if self.my_roads[n1[0]].priority <= self.my_roads[n2[0]].priority:
                                if c < 0:
                                    self.my_roads[n1[0]].stop = True
                            # if n1[1] > 0:
                            #     a = self.my_roads[n1[0]].vectors[n1[1]-1]
                            #     b = self.my_roads[n2[0]].vectors[n2[1]]
                            #     c = a[1] * b[0] - a[0] * b[1]
                            #     if c == -1:
                            #         self.my_roads[n1[0]].stop = True

        # for car1 in cars:
        #     for car2 in cars:
        #         if car1 is not car2:
        #             for i in range(min(len(car1.just_follow_the_orders), len(car2.just_follow_the_orders)) - 1):
        #                 if car1.just_follow_the_orders[i] is car2.just_follow_the_orders[i]:
        #                     car1.stop = True
        #                 if car1.just_follow_the_orders[i] is car2.just_follow_the_orders[i + 1]:
        #                     car1.stop = True

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


# class Signalization:
#     def __init__(self, road_object, time_red=30, time_green=30, starting_state=False):
#         self.time_red = time_red
#         self.time_green = time_green
#         self.road_object = road_object
#
#         self.current_state = starting_state
#         if starting_state is False:
#             self.iterator = 0
#         else:
#             self.iterator = self.time_red + 1
#
#     def cycle(self):
#         self.iterator = self.iterator + 1
#         self.iterator = self.iterator % (self.time_green + self.time_red)
#         if self.iterator > self.time_red:
#             # self.current_state = 1
#             pass
#         else:
#             # self.current_state = 0
#             self.road_object.stop = True
#
#
# class SignalizationObjectList:
#     def __init__(self):
#         self.list_of_lights = []
#
#     def all_lights_cycle(self):
#         for light in self.list_of_lights:
#             light.cycle()
#
#     def add_light(self, signalization_object):
#         self.list_of_lights.append(signalization_object)


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
        new_cars.append(cars[ten].drive())
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
