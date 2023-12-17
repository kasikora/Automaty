import numpy

print("GIIT")

N = 20

matrix = numpy.zeros((N, N))

for i in matrix:
    print(i)

print("\n")
print(matrix)

testarr = numpy.array([[0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])

print(testarr)

print(numpy.shape(testarr))

for i in range(10):
    print(i)


def ar_insert_old(matrix, arToInsert, posx, posy):
    for i in range(numpy.shape(testarr)[0]):
        for j in range(numpy.shape(testarr)[1]):
            matrix[posy + i][posx + j] = arToInsert[i][j]


def ar_insert(matrix, arToInsert, posi, posj):
    matrix[posi:posi + numpy.shape(arToInsert)[0], posj:posj + numpy.shape(arToInsert)[1]] = arToInsert


ar_insert(matrix, testarr, 5, 5)

print(matrix)

arrr = numpy.array([[1, 8, 64], [2, 16, 128], [4, 32, 256]])
arrr2 = numpy.array([[1 << 0, 1 << 3, 1 << 6], [1 << 1, 1 << 4, 1 << 7], [1 << 2, 1 << 5, 1 << 8]])

print(arrr)
print(arrr2)

#
# def every_possible_matrix():
#     n = 3
#     arrays = []
#     for i in range(2 ** (n * n)):
#         binary = bin(i)[2:].zfill(n * n)  # i jako binarny zapis odcinamy 2 pierwsze bo ta jest napisane Ob
#         matrix = numpy.array([int(bit) for bit in binary]).reshape(n, n)
#         arrays.append(matrix)
#     return arrays


# allar = every_possible_matrix()


# for i in allar:
#     print(i, "\n")

def omnipresent_perception():
    n = 3
    neighbours_to_survive_min = 2
    neighbours_to_survive_max = 3
    neighbours_to_become_alive_max = 3
    neighbours_to_become_alive_min = 3
    position_of_me = [1, 1]
    arrays = []
    to_be_or_not_to_be = numpy.zeros(2 ** (n * n))
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
    return to_be_or_not_to_be
    # skoro indexy sa takie jak liczby z ktorych zrobilem maciez to indexy odpowiadaja odpowiednim maciezom :>
    # ponadto maciez jest taka sama w kazda strone wiec jak pojebalem x i y to nie ma problemu :D ?????


dead_or_alive_you_spin_me_right_round = omnipresent_perception()
print(dead_or_alive_you_spin_me_right_round)

number = 1
dimensions = 2

print(matrix)
print("\n")
print(matrix[6-1:6+2, 6-1:6+2])
print((matrix[6-1:6+2, 6-1:6+2] * arrr2).sum())
next_matrix = numpy.zeros((N, N))
for i in range(number, matrix.shape[0] - dimensions * number):
    for j in range(number, matrix.shape[1] - dimensions * number):
        next_matrix[i, j] = dead_or_alive_you_spin_me_right_round[int((matrix[i-1:i+2, j-1:j+2] * arrr2).sum())]

print(matrix)
print("\n")
print(next_matrix)
