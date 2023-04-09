from math import floor

size = int(input())
field = []
player = []
path = []
total_coins = 0
move = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def check_coordinates(*coordinates):
    coordinates = list(coordinates)
    for index in range(len(coordinates)):
        if coordinates[index] == -1:
            coordinates[index] = size - 1
        if coordinates[index] == size:
            coordinates[index] = 0
    return coordinates


for row in range(size):
    current_row = [int(x) if x.isdigit() else x for x in input().split()]
    if 'P' in current_row:
        player = [row, current_row.index('P')]
        path.append(player)
    field.append(current_row)

while True:
    command = input()
    if command not in move.keys():
        continue
    r, c = player[0] + move[command][0], player[1] + move[command][1]
    r, c = check_coordinates(r, c)
    position = field[r][c]
    player = [r, c]
    path.append(player)

    if position == 'X':
        total_coins = floor(total_coins / 2)
        print(f"Game over! You've collected {total_coins} coins.")
        break
    if isinstance(position, int):
        total_coins += position
        field[r][c] = str(position)

    if total_coins >= 100:
        print(f"You won! You've collected {total_coins} coins.")
        break

print("Your path:")
print('\n'.join(str(x) for x in path))
