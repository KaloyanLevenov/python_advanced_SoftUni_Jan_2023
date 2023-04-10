def plant_the_bomb(row, column):
    global field
    field[row][column] = '*'


def how_many_bombs(row, column):
    global field
    moves = ((-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1))

    for x, y in moves:
        a = row + x
        b = column + y
        if not (0 <= a < size and 0 <= b < size):
            continue
        field[row][column] += 1 if field[a][b] == '*' else 0


size = int(input())  # square size matrix
bombs = int(input())  # number of bombs we have to plant
field = [[0] * size for _ in range(size)]  # my empty matrix
bombs_coordinates = [[int(x) for x in input().strip('(').strip(')').split(', ')] for _ in range(bombs)]
[plant_the_bomb(*bombs_coordinates[index]) for index in range(bombs)]
[how_many_bombs(i, j) for i in range(size) for j in range(size) if isinstance(field[i][j], int)]  # i, j are row and col indexes

[print(*field[row]) for row in range(size)]

