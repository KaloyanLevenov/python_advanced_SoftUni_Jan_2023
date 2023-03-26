size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
coordinates = ((int(x) for x in x.split(',')) for x in input().split())
directions = (
    (-1, 0),   # up
    (1, 0),    # down
    (0, 1),    # right
    (0, -1),   # left
    (-1, 1),   # top-right
    (-1, -1),  # top-left
    (1, -1),   # bottom-left
    (1, 1),    # bottom-right
    (0, 0),    # current (this should be last)
)

for row, col in coordinates:
    if matrix[row][col] < 0:
        continue

    for r, c in directions:
        x, y = row + r, col + c
        if 0 <= x < size and 0 <= y < size:
            matrix[x][y] -= matrix[row][col] if matrix[x][y] > 0 else 0

alive_cells = [matrix[row][col] for row in range(size) for col in range(size) if matrix[row][col] > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*matrix[row]) for row in range(size)]
