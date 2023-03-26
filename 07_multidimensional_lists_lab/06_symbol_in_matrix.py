def check_for_symbol(current_matrix, special_symbol):
    for row in range(len(current_matrix)):
        for col in range(len(matrix[row])):
            element = matrix[row][col]
            if element == special_symbol:
                return row, col


def print_func(data):
    if data:
        print(data)
    else:
        print(f"{symbol} does not occur in the matrix")


matrix = [[x for x in input()] for _ in range(int(input()))]
symbol = input()
print_func(check_for_symbol(matrix, symbol))
