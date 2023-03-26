size = int(input())
matrix = [list(input()) for _ in range(size)]
knights_removed = 0

movement = (
    (-2, -1),  # top-left
    (-2, 1),  # top-right
    (-1, -2),  # left-top
    (-1, 2),  # right-top
    (1, -2),  # left-bottom
    (1, 2),  # right-bottom
    (2, -1),  # bottom-left
    (2, 1),  # bottom_right
)
while True:
    has_to_be_removed_knight = []
    most_threatened_knights = 0
    for row in range(size):

        for col in range(size):

            if matrix[row][col] == 'K':
                threatened_knights = 0

                for move in movement:
                    row_move, col_move = move[0], move[1]
                    x, y = row + row_move, col + col_move

                    if not (0 <= x < size and 0 <= y < size):
                        continue

                    threatened_knights += 1 if matrix[x][y] == 'K' else 0

                if threatened_knights > most_threatened_knights:
                    most_threatened_knights = threatened_knights
                    has_to_be_removed_knight = [row, col]  # knight coordinates

    if has_to_be_removed_knight:
        knights_removed += 1
        r, c = has_to_be_removed_knight
        matrix[r][c] = '0'

        continue

    else:
        break

print(knights_removed)
