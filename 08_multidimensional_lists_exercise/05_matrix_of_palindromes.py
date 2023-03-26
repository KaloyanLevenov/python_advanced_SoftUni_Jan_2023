r, c = [int(x) for x in input().split()]
# Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
# Columns + rows define the middle letter:
#        ◦ column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
#      ◦ column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
matrix = []
for row in range(r):
    current_row = []
    for col in range(c):
        element = chr(97 + row)+chr(97 + row + col)+chr(97 + row)
        current_row.append(element)
    matrix.append(current_row)

[print(*matrix[row]) for row in range(r)]

