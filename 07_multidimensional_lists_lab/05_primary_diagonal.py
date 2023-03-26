def primary_diagonal(current_matrix):
    sum_of_primary_diagonal = 0
    for i in range(len(matrix)):
        sum_of_primary_diagonal += matrix[i][i]

    return sum_of_primary_diagonal


matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
print(primary_diagonal(matrix))

