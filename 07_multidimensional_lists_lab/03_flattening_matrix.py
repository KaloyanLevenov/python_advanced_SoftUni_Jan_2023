matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]
flattened_matrix = [element for row in range(len(matrix)) for element in matrix[row]]  # this does the nested for bellow
# for row in range(len(matrix)):
#    for element in matrix[row]:
#        flattened_matrix.append(element)
print(flattened_matrix)
