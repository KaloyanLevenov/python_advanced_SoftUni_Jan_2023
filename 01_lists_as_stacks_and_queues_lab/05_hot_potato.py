from collections import deque
players = deque(input().split())
step = int(input())
while len(players) > 1:
    for _ in range(1,step):
        players.append(players.popleft())
    print(f"Removed {players.popleft()}")
last_kid = players[0]
print(f"Last is {last_kid}")
