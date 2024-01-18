import random
import numpy

numpy.set_printoptions(linewidth=256)

N = 30


class Grain:
    def __init__(self):
        self.center = None
        self.left = None
        self.right = None
        self.val = 0

        self.up_left = None
        self.up_right = None

    def __str__(self):
        return f"{self.val}"

    def __repr__(self):
        return f"{self.val}"

    def fall(self):
        try:
            if self.center.val:
                if -self.left.val + 1 or -self.right.val + 1:
                    self.val = 0
                    chosen_one = \
                        random.choices([self.left, self.right], weights=[-self.left.val + 1, -self.right.val + 1], k=1)[
                            0]
                    chosen_one.val = 1
                    return chosen_one
                else:
                    return self
            else:
                self.val = 0
                self.center.val = 1
                return self.center
        except:
            return self

    def kordyceps(self):
        try:
            if not self.center.val and not self.left.val and not self.right.val:
                chosen_one = random.choices([self.left, self.right, self.center],
                                            weights=[-self.left.val + 1, -self.right.val + 1, -self.center.val + 1],
                                            k=1)[0]
                # chosen_one = random.choice([self.left, self.right, self.center])
                self.val = 0
                chosen_one.val = 1
                return chosen_one
            else:
                return self
        except:
            return self

    def fall3(self):
        try:
            if not self.center.val or not self.left.val or not self.right.val:
                chosen_one = random.choices([self.left, self.right, self.center],
                                            weights=[-self.left.val + 1, -self.right.val + 1, -self.center.val + 1],
                                            k=1)[0]
                # chosen_one = random.choice([self.left, self.right, self.center])
                self.val = 0
                chosen_one.val = 1
                return chosen_one
            else:
                return self
        except:
            return self


matrix = numpy.empty((N, N), dtype=Grain)
for i in range(N):
    for j in range(N):
        matrix[i, j] = Grain()

for i in range(N - 1):
    for j in range(N - 2):
        matrix[i, j + 1].left = matrix[i + 1, j - 1 + 1]
        matrix[i, j + 1].center = matrix[i + 1, j + 1]
        matrix[i, j + 1].right = matrix[i + 1, j + 1 + 1]

print(matrix)
all_sand = []
for i in range(10):
    for j in range(10):
        matrix[i, j + 10].val = 1
        all_sand.append(matrix[i, j + 10])
print("\n", matrix)
# all_sand.reverse()
print(all_sand)


def new_alive_list(matrix, N):
    all_sand = []
    for i in range(N):
        for j in range(N):
            if matrix[i, j].val:
                all_sand.append(matrix[i, j])
    return all_sand


def let_them_fall(all_sand):
    new_sand = []
    for i in all_sand:
        try:
            if i.center.val:
                if -i.left.val + 1 or -i.right.val + 1:
                    i.val = 0
                    chosen_one = random.choices([i.left, i.right], weights=[-i.left.val + 1, -i.right.val + 1], k=1)[0]
                    chosen_one.val = 1
                    new_sand.append(chosen_one)
                else:
                    new_sand.append(i)
            else:
                i.val = 0
                i.center.val = 1
                new_sand.append(i.center)
        except:
            new_sand.append(i)
    return new_sand


def let_them_fall2(all_sand):
    new_sand = []
    while len(all_sand):
        ten = random.randint(0, len(all_sand) - 1)
        new_sand.append(all_sand[ten].fall())
        all_sand.pop(ten)
    return new_sand


def let_them_fall3(all_sand):
    new_sand = []
    random.shuffle(all_sand)
    for i in all_sand:
        new_sand.append(i.fall3())
    return new_sand


# matrix[0, 3].val = 1
# matrix[0, 3].left.val = 1
# matrix[0, 3].center.val = 1
# matrix[0, 3].right.val = 1
# print(matrix)

for i in range(50):
    all_sand = let_them_fall(all_sand)
    print("\n", i, "\n", matrix)
    # print(len(all_sand))

# matrix = []
#
# for i in range(N):
#     matrix.append([])
#     for j in range(N):
#         matrix[i].append(Grain())
#
# print(matrix)


# tab = numpy.array([Grain(), Grain()])
# tab[0].val = 1
# print(tab)
# tab[0].center = tab[1]
# tab[0].center.val = 0
# print(tab)
# tab[0].fall()
# print(tab)


print(~1 + 2, ~0 + 2)
