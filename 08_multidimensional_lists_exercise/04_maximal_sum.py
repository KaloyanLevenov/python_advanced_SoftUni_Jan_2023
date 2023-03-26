rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
biggest_sub_matrix = []
sum_of_biggest_sub_matrix = float('-inf')
for row in range(rows - 2):
    for col in range(columns - 2):
        current_sub_matrix=[]
        current_sub_matrix.extend([matrix[row][col:col + 3]])  #first row of the sub matrix 3x3
        current_sub_matrix.extend([matrix[row + 1][col:col + 3]]) #second row of the sub matrix 3x3
        current_sub_matrix.extend([matrix[row + 2][col:col + 3]]) #third row of the sub matrix 3x3
        sum_of_current_matrix = sum([sum(current_sub_matrix[row]) for row in range(3)])
        if sum_of_current_matrix > sum_of_biggest_sub_matrix:
            biggest_sub_matrix = current_sub_matrix
            sum_of_biggest_sub_matrix = sum_of_current_matrix


print(f'Sum = {sum_of_biggest_sub_matrix}')
[print(*biggest_sub_matrix[row]) for row in range(3)]