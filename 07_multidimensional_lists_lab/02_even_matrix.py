matrix = [[int(x) for x in input().split(', ') if int(x) % 2 == 0] for _ in range(int(input()))]
# Nested comprehension for squared matrix
print(matrix)
