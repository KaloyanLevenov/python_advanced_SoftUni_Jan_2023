from collections import deque

bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
symbols = deque(input().split())
honey_made = 0
honey_calculations = {
    "+": lambda x,y: x + y,
    "-": lambda x,y: x - y,
    "*": lambda x,y: x * y,
    "/": lambda x,y: x /y,
}
while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()
    if nectar >= bee:
        symbol = symbols.popleft()
        honey_made += abs(honey_calculations[symbol](bee,nectar))
    else:
        bees.appendleft(bee)
        continue

print(f"Total honey made: {honey_made}")
print(f"Bees left: {', '.join(str(x) for x in bees)}") if bees else None
print(f"Nectar left: {', '.join(str(x) for x in nectars)}") if nectars else None