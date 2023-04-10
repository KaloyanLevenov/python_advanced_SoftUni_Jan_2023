size = int(input())
field = []
snake = []
lairs = []
food = 0
move = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
for row in range(size):
    current_row = list(input())
    if 'S' in current_row:
        snake = [row, current_row.index('S')]
        current_row[snake[1]] = '.'
    for char in current_row:
        if char == 'B':
            lairs.append([row, current_row.index('B')])
    field.append(current_row)
while food < 10:
    command = input()
    if command not in move.keys():
        continue
    r, c = snake[0] + move[command][0], snake[1] + move[command][1]
    if not (0 <= r < size and 0 <= c < size):
        print("Game over!")
        break
    position = field[r][c]
    snake = [r, c]
    field[r][c] = '.'
    if position == '*':
        food += 1
    elif position == 'B':
        if snake == lairs[0]:
            snake = lairs[1]
        elif snake == lairs[1]:
            snake = lairs[0]
        field[snake[0]][snake[1]] = '.'

else:
    print("You won! You fed the snake.")
    field[snake[0]][snake[1]] = 'S'
print(f"Food eaten: {food}")
[print(*field[row], sep='') for row in range(size)]