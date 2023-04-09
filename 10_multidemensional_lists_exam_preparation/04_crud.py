def create_func(mx, commands, coordinates):
    direction, value = commands
    r, c = motion[direction][0] + coordinates[0], motion[direction][1] + coordinates[1]
    position = mx[r][c]

    if position == '.':
        mx[r][c] = value

    coordinates = [r, c]

    return coordinates


def update_func(mx, commands, coordinates):
    direction, value = commands
    r, c = motion[direction][0] + coordinates[0], motion[direction][1] + coordinates[1]
    position = mx[r][c]

    if position.isalnum():
        mx[r][c] = value

    coordinates = [r, c]

    return coordinates


def delete_func(mx, direction, coordinates):
    r, c = motion[direction][0] + coordinates[0], motion[direction][1] + coordinates[1]
    position = mx[r][c]

    if position.isalnum():
        mx[r][c] = '.'

    coordinates = [r, c]

    return coordinates


def read_func(mx, direction, coordinates):
    r, c = motion[direction][0] + coordinates[0], motion[direction][1] + coordinates[1]
    position = mx[r][c]

    if position.isalnum():
        print(position)

    coordinates = [r, c]

    return coordinates


size = 6
matrix = [input().split() for _ in range(size)]
position = list(map(int, list(filter(lambda x: x.isdigit(), list(input())))))

command = input().split(', ')

motion = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while command[0] != 'Stop':

    if command[0] == 'Create':
        position = create_func(matrix, command[1:], position)
    elif command[0] == 'Update':
        position = update_func(matrix, command[1:], position)
    elif command[0] == 'Delete':
        position = delete_func(matrix, command[1], position)
    elif command[0] == 'Read':
        position = read_func(matrix, command[1], position)

    command = input().split(', ')

[print(*matrix[row]) for row in range(size)]