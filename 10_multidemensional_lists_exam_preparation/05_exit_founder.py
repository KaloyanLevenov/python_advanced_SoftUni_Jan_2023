SIZE = 6
EXIT = 'E'
TRAP = 'T'
WALL = 'W'
EMPTY_POSITION = '.'
penalty = False
skip_turn = False
current_player_coordinates = []
second_player_coordinates = []

current_player, second_player = input().split(', ')
maze = [input().split() for _ in range(SIZE)]


def swap_players():
    global penalty
    global current_player_coordinates
    global second_player_coordinates
    global current_player
    global second_player
    global skip_turn

    if penalty:
        penalty = False
        skip_turn = True

    current_player, second_player = second_player, current_player
    current_player_coordinates, second_player_coordinates = second_player_coordinates, current_player_coordinates


while True:

    row, col = [int(x) for x in input().strip('(').strip(')').split(', ')]

    if skip_turn:
        skip_turn = False
        swap_players()
        continue

    current_player_coordinates = [row, col]
    player = current_player

    if maze[row][col] == 'E':
        print(f"{player} found the Exit and wins the game!")
        break
    elif maze[row][col] == TRAP:
        print(f"{player} is out of the game! The winner is {second_player}.")
        break
    elif maze[row][col] == WALL:
        print(f"{player} hits a wall and needs to rest.")
        swap_players()
        penalty = True
        continue

    swap_players()