def make_matrix():
    current_matrix = []
    rows, cols = map(int, input().split(', '))
    for row in range(rows):
        row_data = list(map(int, input().split(', ')))
        current_matrix.append(row_data)
    return current_matrix


def sum_matrix_elements(current_matrix):
    sum_of_matrix_elements = 0
    for row in range(len(current_matrix)):
        sum_of_matrix_elements += sum(current_matrix[row])

    print(sum_of_matrix_elements)


matrix = make_matrix() # Creating the matrix from input data
sum_matrix_elements(matrix) # summarising the elements
print(matrix)

