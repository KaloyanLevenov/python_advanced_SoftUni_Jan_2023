size = int(input())
matrix = [[int(number) for number in input().split()] for _ in range(size)]
command = [int(x) if x.isdigit() else x for x in input().split()]
calculations = {
    'Add': lambda x, y: x + y,
    'Subtract': lambda x, y: x - y,
}
while command[0] != 'END':
    action, row, col, number = command

    if not (0 <= int(row) < size and 0 <= int(col) < size):
        print('Invalid coordinates')
    else:
        matrix[row][col] = calculations[action](matrix[row][col], number)

    command = [int(x) if x.isdigit() else x for x in input().split()]
else:
    [print(*matrix[row]) for row in range(size)]