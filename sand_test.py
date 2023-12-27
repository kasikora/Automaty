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

    def __str__(self):
        return f"{self.val}"

    def __repr__(self):
        return f"{self.val}"

    def fall(self):
        if self.center.val:
            pass
        else:
            self.center.val = 1
            self.val = 0


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
all_sand.reverse()
print(all_sand)


def let_them_fall(all_sand):
    new_sand = []
    for i in all_sand:
        try:
            if i.center.val:
                if -i.left.val+1 or -i.right.val+1:
                    chosen_one = random.choices([i.left, i.right], weights=[-i.left.val+1, -i.right.val+1], k=1)[0]
                    chosen_one.val = 1
                    new_sand.append(chosen_one)
                else:
                    pass
            else:
                i.val = 0
                i.center.val = 1
                new_sand.append(i.center)
        except:
            new_sand.append(i)
    return new_sand


for i in range(50):
    all_sand = let_them_fall(all_sand)
    print("\n", i, "\n", matrix)
    #print(len(all_sand))

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


print(~1+2, ~0+2)