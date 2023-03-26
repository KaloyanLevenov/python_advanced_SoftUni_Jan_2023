move_register = {
    'right': lambda x, y, z: (x, y + z) if (y + z) < size and field[x][y + z] != 'x' else (x, y),
    'left': lambda x, y, z: (x, y - z) if (y - z) >= 0 and field[x][y - z] != 'x' else (x, y),
    'up': lambda x, y, z: (x - z, y) if (x - z) >= 0 and field[x - z][y] != 'x' else (x, y),
    'down': lambda x, y, z: (x + z, y) if (x + z) < size and field[x + z][y] != 'x' else (x, y),
}

shoot_register = {
    'right': (0, 1),
    'left': (0, -1),
    'up': (-1, 0),
    'down': (1, 0),
}

size = 5
field = []
targets_to_shoot = 0
targets_shot = 0
targets_coordinates = []
position = ()
for row in range(size):
    current_row = [int(x) if x.isdigit() else x for x in input().split()]

    if 'A' in current_row:
        position = row, current_row.index('A')
        current_row[current_row.index('A')] = '.'

    if 'x' in current_row:
        targets_to_shoot += current_row.count('x')

    field.append(current_row)

for _ in range(int(input())):
    command = input().split()

    if 'move' in command:
        direction = command[1]
        steps = int(command[2])
        position = move_register[direction](position[0], position[1], steps)


    elif 'shoot' in command:
        direction = command[1]
        r = position[0] + shoot_register[direction][0]
        c = position[1] + shoot_register[direction][1]
        while 0 <= r < size and 0 <= c < size:

            if field[r][c] == 'x':
                field[r][c] = '.'
                targets_to_shoot -= 1
                targets_shot += 1
                targets_coordinates.append([r, c])
                break

            r += shoot_register[direction][0]
            c += shoot_register[direction][1]

    if targets_to_shoot == 0:
        print(f"Training completed! All {targets_shot} targets hit.")
        break


else:
    print(f"Training not completed! {targets_to_shoot} targets left.")

print(*targets_coordinates, sep='\n') if targets_coordinates else None