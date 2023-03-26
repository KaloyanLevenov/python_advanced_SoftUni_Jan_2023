def primary(current_matrix):
    sum = 0
    diagonal = []
    for row in range(len(current_matrix)):
        col = row
        sum += current_matrix[row][col]
        diagonal.append(current_matrix[row][col])
    return sum, diagonal


def secondary(current_matrix):
    sum = 0
    diagonal = []
    for row in range(len(current_matrix)):
        col = (len(current_matrix) - 1) - row
        sum += current_matrix[row][col]
        diagonal.append(current_matrix[row][col])
    return sum, diagonal



matrix = [ [int(x) for x in input().split(', ')] for _ in range(int(input()))]
sum_of_primary, primary_diagonal = primary(matrix)
sum_of_secondary, secondary_diagonal = secondary(matrix)

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum_of_primary}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum_of_secondary}")