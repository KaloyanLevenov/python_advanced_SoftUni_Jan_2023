matrix = [[int(x) for x in x.split()] for x in input().split('|')[::-1]]
[print(matrix[row][col], end=' ') for row in range(len(matrix)) for col in range(len(matrix[row]))]