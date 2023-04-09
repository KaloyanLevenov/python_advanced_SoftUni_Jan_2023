size = int(input())
battlefield = []
submarine = []
naval_mines = 0
battle_cruisers = 0

for row in range(size):
    current_row = list(input())
    if 'S' in current_row:
        submarine = [row, current_row.index('S')]
        current_row[current_row.index('S')] = '-'
    battlefield.append(current_row)

motion = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while battle_cruisers != 3:
    command = input()

    r = submarine[0] + motion[command][0]
    c = submarine[1] + motion[command][1]

    position = battlefield[r][c]  # what is on the new position
    battlefield[r][c] = '-'  # when stepping it goes '-'
    submarine = [r, c]  # re writing the new coordinates

    if position == '*':
        naval_mines += 1
    elif position == 'C':
        battle_cruisers += 1
        battlefield[r][c] = 'S' if battle_cruisers == 3 else '-'

    if naval_mines == 3:
        battlefield[r][c] = 'S'
        break

else:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!") if naval_mines == 3 else None
[print(''.join(battlefield[row])) for row in range(len(battlefield))]