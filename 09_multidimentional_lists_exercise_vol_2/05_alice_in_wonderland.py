size = int(input())
field = []
alice_coordinates = []
bags_of_tea_collected = 0
out_of_field = False
stepped_on_rabbit_hole = False

for row in range(size):
    current_row = input().split()

    if 'A' in current_row:
        alice_coordinates = [row, current_row.index('A')]
        current_row[current_row.index('A')] = '*'

    field.append(current_row)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while bags_of_tea_collected < 10:
    command = input()
    r = alice_coordinates[0] + directions[command][0]
    c = alice_coordinates[1] + directions[command][1]

    if not (0 <= r < size and 0 <= c < size):
        out_of_field = True
        break

    alice_coordinates = [r, c]
    alice_position = field[r][c]
    field[r][c] = '*'

    if alice_position == 'R':
        stepped_on_rabbit_hole = True
        break

    if alice_position.isdigit():
        bags_of_tea_collected += int(alice_position)

else:
    print("She did it! She went to the party.")
    [print(*field[row]) for row in range(size)]

if out_of_field or stepped_on_rabbit_hole:
    print("Alice didn't make it to the tea party.")
    [print(*field[row]) for row in range(size)]
