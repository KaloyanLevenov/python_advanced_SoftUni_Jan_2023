def make_matrix():
    rows, cols = list(map(int, input().split(', ')))
    current_matrix = []
    for row in range(rows):
        current_row = list(map(int, input().split()))
        current_matrix.append(current_row)
    return rows, cols, current_matrix


def sum_matrix_columns(rows, cols, matrix):
    for column in range(cols):
        sum_of_column = 0
        for row in range(rows):
            element = matrix[row][column]
            sum_of_column += element
        print(sum_of_column)


rows, cols, matrix = make_matrix()
sum_matrix_columns(rows, cols, matrix)
