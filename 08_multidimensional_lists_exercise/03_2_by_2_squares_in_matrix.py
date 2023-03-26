rows, columns = list(map(int, input().split()))
matrix = [input().split() for _ in range(rows)]
sub_matrix_counter = 0

for row in range(len(matrix) - 1):
    for col in range(len(matrix[row]) - 1):
        sub_matrix = [
            matrix[row][col], matrix[row][col + 1],
            matrix[row + 1][col], matrix[row + 1][col + 1]
        ]
        if sub_matrix.count(sub_matrix[0]) == len(sub_matrix):
            sub_matrix_counter += 1

print(sub_matrix_counter)

        ##### Solution with numpy library####
# #import numpy
# #rows, collumns = list(map(int, input().split()))
# matrix = numpy.array([input().split() for _ in range(rows)])
# sub_matrix_counter = 0
#
# for row in range(len(matrix) - 1):
#     for col in range(len(matrix[row]) - 1):
#         sub_matrix = matrix[row:(row + 2),col:(col + 2)]
#         sub_matrix = numpy.ravel(sub_matrix) #flattened the 2D array into 1D
#         if numpy.all(sub_matrix==sub_matrix[0]):
#             sub_matrix_counter += 1
#
# print(sub_matrix_counter)
