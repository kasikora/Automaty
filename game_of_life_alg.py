import numpy

numpy.set_printoptions(linewidth=256)


def omnipresent_perception(neighbours_to_survive_min=2, neighbours_to_survive_max=3, neighbours_to_become_alive_max=3, neighbours_to_become_alive_min=3, position_of_me=[1, 1]):
    n = 3
    # neighbours_to_survive_min = 2
    # neighbours_to_survive_max = 3
    # neighbours_to_become_alive_max = 3
    # neighbours_to_become_alive_min = 3
    # position_of_me = [1, 1]

    stuff = []
    to_be_or_not_to_be = numpy.zeros(2 ** (n * n)).astype(numpy.int16) - 1
    for i in range(2 ** (n * n)):
        binary = bin(i)[2:].zfill(n * n)  # i jako binarny odcinamy 2 pierwsze bo ta jest napisane Ob
        matrix = numpy.array([int(bit) for bit in binary]).reshape(n, n)
        sum_of_matix = matrix.sum()
        if matrix[position_of_me[0], position_of_me[1]] == 1:
            if sum_of_matix - 1 > neighbours_to_survive_max or sum_of_matix - 1 < neighbours_to_survive_min:
                to_be_or_not_to_be[i] = 0
            else:
                to_be_or_not_to_be[i] = 1
        else:
            if sum_of_matix > neighbours_to_become_alive_max or sum_of_matix < neighbours_to_become_alive_min:
                to_be_or_not_to_be[i] = 0
            else:
                to_be_or_not_to_be[i] = 1
    tmp = numpy.zeros((n * n)).astype(numpy.int16)
    print(tmp)
    for i in range(n * n):
        tmp[i] = (1 << n * n - i - 1)
    template_matrix = tmp.reshape(n, n).astype(numpy.int16)

    print("------------------")
    print(template_matrix)
    stuff.append(to_be_or_not_to_be)
    stuff.append(template_matrix)
    return stuff


def next_matrix(matrix, N, dead_or_alive, arr):
    number = 1
    dimensions = 2
    new_matrix = numpy.zeros((N, N)).astype(numpy.int16)
    for i in range(number, matrix.shape[0] - dimensions * number):
        for j in range(number, matrix.shape[1] - dimensions * number):
            new_matrix[i, j] = dead_or_alive[int((matrix[i - 1:i + 2, j - 1:j + 2] * arr).sum())]
    return new_matrix


def ar_insert(matrix, arToInsert, posi, posj):
    matrix[posi:posi + numpy.shape(arToInsert)[0], posj:posj + numpy.shape(arToInsert)[1]] = arToInsert


## example of use
N = 20

# wymuszam poczotkowy stan
matrix = numpy.zeros((N, N)).astype(numpy.int16)
testarr = numpy.array([[0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
ar_insert(matrix, testarr, 10, 10)

# wlasciwa czesc
data = omnipresent_perception()  # mozna podac argumety zeby zmnienic zasady gry
dead_or_alive = data[0]
arr = data[1]
print(matrix)
for i in range(50):
    matrix = next_matrix(matrix, N, dead_or_alive, arr)
    print(i)
    print(matrix, "\n")

