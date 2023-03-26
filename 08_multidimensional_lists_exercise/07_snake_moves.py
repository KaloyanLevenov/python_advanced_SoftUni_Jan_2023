from collections import deque

rows, columns = [int(x) for x in input().split()]
snake_string = list(input())
string_copy = deque(snake_string)
matrix = []
for row in range(rows):
    current_row = deque()
    while len(string_copy) < columns:
        string_copy.extend(snake_string)
    for col in range(columns):
        if row % 2 == 0:
            current_row.append(string_copy.popleft())
        else:
            current_row.appendleft(string_copy.popleft())

    matrix.append(list(current_row))

[print(*matrix[row], sep= "") for row in range(rows)]


