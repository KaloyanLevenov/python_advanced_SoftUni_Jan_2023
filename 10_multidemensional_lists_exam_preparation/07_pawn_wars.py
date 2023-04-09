size = 8
field = []
column = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
white_pawn = []
black_pawn = []
queen_will_happen = False
for row in range(size):
    current_row = input().split(' ')
    if 'w' in current_row:
        white_pawn = [row, current_row.index('w')]
    elif 'b' in current_row:
        black_pawn = [row, current_row.index('b')]
    field.append(current_row)

while True:
    white_pawn[0] -= 1
    if white_pawn[0] == 0:
        print(f"Game over! White pawn is promoted to a queen at {column[white_pawn[1]]}8.")
        break
    elif white_pawn[0] == black_pawn[0] and abs((white_pawn[1] - black_pawn[1])) == 1:
        white_pawn[1] = black_pawn[1]
        square = column[white_pawn[1]] + str(8 - white_pawn[0])
        print(f"Game over! White win, capture on {square}.")
        break

    black_pawn[0] += 1
    if black_pawn[0] == 7:
        print(f"Game over! Black pawn is promoted to a queen at {column[black_pawn[1]]}1.")
        break

    elif black_pawn[0] == white_pawn[0] and abs((white_pawn[1] - black_pawn[1])) == 1:
        black_pawn[1] = white_pawn[1]
        square = column[black_pawn[1]] + str(8 - black_pawn[0])
        print(f"Game over! Black win, capture on {square}.")
        break

