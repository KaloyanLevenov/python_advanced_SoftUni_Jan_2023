matrix = []
rows, columns = list(map(int, input().split(', ')))

for row in range(rows):
    current_row = list(map(int, input().split(', ')))
    matrix.append(current_row)

sub_matrix = []
sum_of_sub_matrix = 0
for row in range(len(matrix) - 1):
    for col in range(len(matrix[row]) - 1):
        # creating sub matrix 2x2 with the following elements
        top_left_element = matrix[row][col]
        top_right_element = matrix[row][col + 1]
        bottom_left_element = matrix[row + 1][col]
        bottom_right_element = matrix[row + 1][col + 1]
        current_sub_matrix = [[top_left_element, top_right_element], [bottom_left_element, bottom_right_element]]
        sum_of_current_sub_matrix = sum(sum(row) for row in current_sub_matrix)
        if sum_of_current_sub_matrix > sum_of_sub_matrix:
            sum_of_sub_matrix = sum_of_current_sub_matrix
            sub_matrix = current_sub_matrix

for row in sub_matrix:
    print(' '.join(str(x) for x in row))
print(sum_of_sub_matrix)

