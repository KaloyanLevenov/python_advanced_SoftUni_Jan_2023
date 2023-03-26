m = int(input())  # number of presents
n = int(input())  # the size of the neighborhood with a square shape
neighborhood = []
nice_kids_without_presents = 0
nice_kids_with_presents = 0
position = []
for row in range(n):
    current_row = input().split()

    if "V" in current_row:
        nice_kids_without_presents += current_row.count('V')

    if "S" in current_row:
        position = [row, current_row.index('S')]
        current_row[current_row.index('S')] = "-"

    neighborhood.append(current_row)

motion = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:

    command = input()
    if m == 0 or command == 'Christmas morning':
        break

    r = position[0] + motion[command][0]
    c = position[1] + motion[command][1]

    if not (0 <= r < n and 0 <= c < n):
        continue

    neighborhood[position[0]][position[1]] = '-'
    position = [r, c]
    state = neighborhood[r][c]
    neighborhood[r][c] = "S"

    if state == 'C':

        for move in motion.values():
            a = position[0] + move[0]
            b = position[1] + move[1]

            if not (0 <= a < n and 0 <= b < n):
                continue

            if neighborhood[a][b] != '-':
                m -= 1
                if neighborhood[a][b] == 'V':
                    nice_kids_with_presents += 1
                    nice_kids_without_presents -= 1
                neighborhood[a][b] = '-'
                if m == 0:
                    break

    elif state == 'V':
        m -= 1
        nice_kids_with_presents += 1
        nice_kids_without_presents -= 1

    elif state == 'X':
        pass

    if m == 0:
        print("Santa ran out of presents!") if nice_kids_without_presents else None
        break

[print(*neighborhood[row]) for row in range(n)]

if not nice_kids_without_presents:
    print(f"Good job, Santa! {nice_kids_with_presents} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_without_presents} nice kid/s.")