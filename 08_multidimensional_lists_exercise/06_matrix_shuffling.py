rows, columns = [int(x) for x in input().split()]
valid_rows = range(rows)
valid_columns = range(columns)
matrix = [input().split() for _ in range(rows)]
command = input()
while command != 'END':
    command_is_valid = False
    coordinates_are_valid = False
    key_word, *coordinates = [int(x) if x.isdigit() else x for x in command.split()]
    if key_word == 'swap' and len(coordinates) == 4:
        command_is_valid = True
        if {coordinates[0], coordinates[2]}.issubset(valid_rows) and {coordinates[1], coordinates[3]}.issubset(
                valid_columns):
            coordinates_are_valid = True

    if command_is_valid and coordinates_are_valid:
        row_one, col_one, row_two, col_two = coordinates
        matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
        [print(*matrix[row]) for row in range(rows)]
    else:
        print('Invalid input!')

    command = input()
