SIZE = 6
matrix = []
rover = []
deposit_register = {
    'W': 0,
    'M': 0,
    'C': 0,
}
deposit_name = {
    'W': 'Water',
    'M': 'Metal',
    'C': 'Concrete',
}
motion = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(SIZE):
    current_row = input().split()
    if 'E' in current_row:
        rover = [row, current_row.index('E')]
    matrix.append(current_row)

commands = input().split(', ')

for command in commands:
    r, c = motion[command][0] + rover[0], motion[command][1] + rover[1]

    if r == -1:
        r = 5
    elif r == 6:
        r = 0
    elif c == -1:
        c = 5
    elif c == 6:
        c = 0

    rover = [r, c]
    position = matrix[r][c]

    if position == 'R':
        print(f"Rover got broken at ({r}, {c})")
        break

    if position in deposit_register.keys():
        deposit_register[position] += 1
        print(f"{deposit_name[position]} deposit found at ({r}, {c})")

suitable_for_colony = all([value >= 1 for value in deposit_register.values()])

if suitable_for_colony:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')