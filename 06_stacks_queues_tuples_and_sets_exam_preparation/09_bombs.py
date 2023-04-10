from collections import deque


def make_bomb(bomb):
    global bombs_made
    bombs_made[bomb] += 1


register = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs',
}
bombs_made = {
    'Datura Bombs':0,
    'Cherry Bombs':0,
    'Smoke Decoy Bombs':0,
}
bombs_are_ready = False
bomb_effects = deque(map(int, input().split(', ')))
bomb_casings = list(map(int, input().split(', ')))

while bomb_casings and bomb_effects:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()
    total = effect + casing

    if total in register.keys():
        make_bomb(register[total])
        bombs_are_ready = all(value >= 3 for value in bombs_made.values())
        if bombs_are_ready:
            break
    else:
        bomb_casings.append(casing - 5)
        bomb_effects.appendleft(effect)

if bombs_are_ready:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")


[print(f"{key}: {value}") for key, value in sorted(bombs_made.items())]