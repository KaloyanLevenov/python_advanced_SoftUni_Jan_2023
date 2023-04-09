n, m = [int(x) for x in input().split()]
playground = []
my_coordinates = []
touched_oponents = 0
moves_made = 0
for row in range(n):
    current_row = input().split()
    if 'B' in current_row:
        my_coordinates = [row, current_row.index('B')]
    playground.append(current_row)
motion = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while touched_oponents != 3:
    command = input()

    if command == 'Finish':
        break

    r = my_coordinates[0] + motion[command][0]
    c = my_coordinates[1] + motion[command][1]

    if not (0 <= r < n and 0 <= c < m):
        continue
    elif playground[r][c] == 'O':
        continue
    elif playground[r][c] == 'P':
        touched_oponents += 1

    playground[my_coordinates[0]][my_coordinates[1]] = '-'
    my_coordinates = [r, c]
    playground[r][c] = 'B'
    moves_made += 1

print("Game over!")
print(f"Touched opponents: {touched_oponents} Moves made: {moves_made}")