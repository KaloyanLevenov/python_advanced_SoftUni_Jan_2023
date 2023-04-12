def make_matrix():
    matrix = []
    player = []
    for row in range(size):
        current_row = list(input())
        if 's' in current_row:
            player = [row, current_row.index('s')]
        matrix.append(current_row)
    return matrix, player


move = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

size = int(input())
commands = input().split(', ')
field, squirrel = make_matrix()
hazelnuts = 0

while commands:
    command = commands.pop(0)
    r, c = squirrel[0] + move[command][0], squirrel[1] + move[command][1]

    if not(0 <= r < size and 0 <= c < size):
        print("The squirrel is out of the field.")
        break

    squirrel = [r, c]
    position = field[r][c]

    if position == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    elif position == 'h':
        hazelnuts += 1
        field[r][c] = '*'
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break

else:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")