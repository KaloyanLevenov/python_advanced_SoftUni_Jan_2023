size = int(input())
car_number = input()
car_coordinates = [0, 0]
tunnel_coordinates = []
matrix = []
kilometers_passed = 0

for row in range(size):
    current_row = input().split()
    for element in current_row:
        if element == 'T':
            tunnel_coordinates.append([row, current_row.index('T')])
    matrix.append(current_row)

motion = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    command = input()

    if command == 'End':
        print(f"Racing car {car_number} DNF.")
        matrix[car_coordinates[0]][car_coordinates[1]] = 'C'
        break

    r = car_coordinates[0] + motion[command][0]
    c = car_coordinates[1] + motion[command][1]

    position = matrix[r][c]  # what is on the new position
    car_coordinates = [r, c]  # re writing the new coordinates

    if position == 'T':
        first_entrance, second_entrance = tunnel_coordinates

        if car_coordinates == first_entrance:
            car_coordinates = second_entrance
        else:
            car_coordinates = first_entrance
        matrix[first_entrance[0]][first_entrance[1]] = '.'
        matrix[second_entrance[0]][second_entrance[1]] = '.'

        kilometers_passed += 30

    elif position == 'F':
        print(f"Racing car {car_number} finished the stage!")
        matrix[r][c] = 'C'
        kilometers_passed += 10
        break

    else:
        kilometers_passed += 10

print(f"Distance covered {kilometers_passed} km.")
[print(f'{"".join(matrix[row])}') for row in range(len(matrix))]