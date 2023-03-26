def primary(current_matrix):
    sum = 0
    for row in range(len(matrix)):
        col = row
        sum += current_matrix[row][col]
    return sum


def secondary(current_matrix):
    sum = 0
    for row in range(len(matrix)):
        col = (len(matrix) - 1) - row
        sum += current_matrix[row][col]
    return sum


matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
primary_sum, secondary_sum = primary(matrix), secondary(matrix)
result = abs(primary_sum - secondary_sum)
print(result)