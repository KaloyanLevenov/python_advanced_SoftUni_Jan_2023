size_of_field = int(input())
field = []
bunny_start_position = []
most_collected_eggs = 0
best_move = None
best_coordinates = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size_of_field):
    current_row = input().split()

    if 'B' in current_row:
        bunny_start_position = [row, current_row.index('B')]

    field.append(current_row)

for move, coordinates in directions.items():
    current_move = move # just for info
    pos_row, pos_col = coordinates  # coordinates of the current move
    curr_row, curr_col = bunny_start_position[0] + pos_row, bunny_start_position[1] + pos_col  # coordinates of next pos
    collected_eggs = 0
    current_coordinates = []

    while 0 <= curr_row < size_of_field and 0 <= curr_col < size_of_field and field[curr_row][curr_col] != 'X':
        collected_eggs += int(field[curr_row][curr_col])
        current_coordinates.append([curr_row,curr_col])
        curr_row += pos_row
        curr_col += pos_col  # if we are in the field and not on trap, we step forward, increasing the coordinates

    if collected_eggs >= most_collected_eggs :
        most_collected_eggs = collected_eggs
        best_move = current_move
        best_coordinates = current_coordinates

print(best_move)
[print(best_coordinates[row]) for row in range(len(best_coordinates))]
print(most_collected_eggs)



