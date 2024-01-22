import time

import numpy

numpy.set_printoptions(linewidth=256)

print("GIIT")

N = 100

matrix = numpy.zeros((N, N)).astype(numpy.int16)

for i in matrix:
    print(i)

print("\n")
print(matrix)

testarr = numpy.array([[0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])

print(testarr)

print(numpy.shape(testarr))


def ar_insert_old(matrix, arToInsert, posx, posy):
    for i in range(numpy.shape(testarr)[0]):
        for j in range(numpy.shape(testarr)[1]):
            matrix[posy + i][posx + j] = arToInsert[i][j]


def ar_insert(matrix, arToInsert, posi, posj):
    matrix[posi:posi + numpy.shape(arToInsert)[0], posj:posj + numpy.shape(arToInsert)[1]] = arToInsert


ar_insert(matrix, testarr, 10, 10)
# testarr = numpy.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]])
# ar_insert(matrix, testarr, 0, 0)

print(matrix)

arrr = numpy.array([[1, 8, 64], [2, 16, 128], [4, 32, 256]]).astype(numpy.int16)
arrr2 = numpy.array([[1 << 0, 1 << 3, 1 << 6], [1 << 1, 1 << 4, 1 << 7], [1 << 2, 1 << 5, 1 << 8]]).astype(numpy.int16)
arrr3 = numpy.array([[0, 3, 6], [1, 4, 7], [2, 5, 8]])

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
    # skoro indexy sa takie jak liczby z ktorych zrobilem maciez to indexy odpowiadaja odpowiednim maciezom :>
    # ponadto maciez jest taka sama w kazda strone wiec jak pojebalem x i y to nie ma problemu :D ?????


def next_matrix(matrix, dead_or_alive, arr):
    number = 1
    dimensions = 2
    new_matrix = numpy.zeros((N, N)).astype(numpy.int16)
    for i in range(number, matrix.shape[0] - dimensions * number):
        for j in range(number, matrix.shape[1] - dimensions * number):
            new_matrix[i, j] = dead_or_alive[int((matrix[i - 1:i + 2, j - 1:j + 2] * arr).sum())]
    return new_matrix


print(matrix)
print("\n")


def next_matrix2(matrix):
    position_of_me = [1, 1]
    neighbours_to_survive_min = 2
    neighbours_to_survive_max = 3
    neighbours_to_become_alive_max = 3
    neighbours_to_become_alive_min = 3
    new_matrix = numpy.array((matrix.shape[0], matrix.shape[1]))
    number = 1
    dimensions = 2
    new_matrix = numpy.zeros((N, N), dtype=numpy.int8)
    for i in range(number, matrix.shape[0] - dimensions * number):
        for j in range(number, matrix.shape[1] - dimensions * number):
            sum_of_matix = (matrix[i - 1:i + 2, j - 1:j + 2]).sum()
            if matrix[position_of_me[0], position_of_me[1]] == 1:
                if sum_of_matix - 1 > neighbours_to_survive_max or sum_of_matix - 1 < neighbours_to_survive_min:
                    new_matrix[i, j] = 0
                else:
                    new_matrix[i, j] = 1
            else:
                if sum_of_matix > neighbours_to_become_alive_max or sum_of_matix < neighbours_to_become_alive_min:
                    new_matrix[i, j] = 0
                else:
                    new_matrix[i, j] = 1
    return new_matrix


# tmp = omnipresent_perception()
# dead_or_alive_you_spin_me_right_round = tmp[0]
# arrr4 = tmp[1]
# print(dead_or_alive_you_spin_me_right_round.dtype)
# print(arrr4)
# matrix1 = matrix.copy()
#
# start_time = time.time()
# for i in range(25):
#     matrix1 = next_matrix2(matrix1)
#
#     # print(i)
#     # print(matrix, "\n")
# print("z ifami")
# print(time.time()-start_time)

# matrix2 = matrix.copy()
# start_time = time.time()

# for i in range(50):
#     matrix2 = next_matrix(matrix2, dead_or_alive_you_spin_me_right_round, arrr4)
#     # print(i)
#     # print(matrix2, "\n")
# print("bez ifow")
# print(time.time() - start_time)
print("------------")

#  i   j
a=[-1,  1]
b=[1, 1]
# todo matma na to czy przyjechal z prawej czy z lewej
c=[0,0]
c[0]=a[0]*b[0]+a[1]*b[1]
c[1]=a[1]*b[0]-a[0]*b[1]
print(c)
#
# list_of_lists = [
#     [1, 2, 3, 4],
#     [3, 4, 5, 6],
#     [7, 8, 9, 10],
#     [3, 4, 11, 12]
# ]
#
# # Create a dictionary to store the indices of each element
# element_indices = {}
#
# # Iterate through each list in the list of lists
# for list_index, sublist in enumerate(list_of_lists):
#     # Iterate through each element in the sublist
#     for element_index, element in enumerate(sublist):
#         # If the element is already in the dictionary, add the current index
#         if element in element_indices:
#             element_indices[element].append((list_index, element_index))
#         else:
#             # Otherwise, create a new list for the element with the current index
#             element_indices[element] = [(list_index, element_index)]
#
# # Filter elements that appear in more than one sublist
# common_elements = {element: indices for element, indices in element_indices.items() if len(indices) > 1}
#
# # Print the common elements and their occurrences
# for element, indices_list in common_elements.items():
#     print(f"Element {element} appears in:")
#     for list_index, element_index in indices_list:
#         print(f"  List {list_index} at index {element_index}")

