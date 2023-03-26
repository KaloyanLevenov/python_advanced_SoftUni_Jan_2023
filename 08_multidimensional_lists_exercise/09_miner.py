from collections import deque

size = int(input())
commands = deque(input().split())
field = [input().split() for _ in range(size)]
miner_moves = {'left': (0, -1),  # "left", "right", "up" and "down"
               'right': (0, 1),
               'up': (-1, 0),
               'down': (1, 0),
               }
miner_coordinates = []
coal_in_the_field = 0
coal_collected = 0
for row in range(size):  # searching where is the miner in the field
    for col in range(size):
        element = field[row][col]
        if element == 's':
            miner_coordinates.extend([row, col])
        if element == 'c':
            coal_in_the_field += 1

while commands:
    current_command = commands.popleft()
    r, c = miner_moves[current_command]
    current_row = miner_coordinates[0] + r
    current_column = miner_coordinates[1] + c

    if 0 <= current_row < size and 0 <= current_column < size:
        field[miner_coordinates[0]][miner_coordinates[1]], field[current_row][current_column] = field[current_row][
            current_column], field[miner_coordinates[0]][miner_coordinates[1]]
