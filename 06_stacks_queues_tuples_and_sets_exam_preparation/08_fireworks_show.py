from collections import deque


def make_fireworks(register, key):
    register[key] += 1


firework_effects = deque(int(x) for x in input().split(', ') if int(x) > 0)
explosive_power = [int(x) for x in input().split(', ') if int(x) > 0]
fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
prepared_enough_fireworks = False
while True:
    if not firework_effects or not explosive_power:
        break
    effect = firework_effects.popleft()
    if effect == 0:
        continue
    power = explosive_power.pop()
    if power == 0:
        continue
    total = effect + power

    if total % 3 == 0 and total % 5 != 0:
        make_fireworks(fireworks, 'Palm Fireworks')
    elif total % 3 != 0 and total % 5 == 0:
        make_fireworks(fireworks, 'Willow Fireworks')
    elif total % 3 == 0 and total % 5 == 0:
        make_fireworks(fireworks, 'Crossette Fireworks')
    else:
        firework_effects.append(effect - 1)
        explosive_power.append(power)

    prepared_enough_fireworks = all(value >= 3 for value in fireworks.values())
    if prepared_enough_fireworks:
        break


print("Congrats! You made the perfect firework show!") if prepared_enough_fireworks else print(
    "Sorry. You can't make the perfect firework show.")
print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}") if firework_effects else None
print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}") if explosive_power else None
[print(f"{key}: {value}") for key, value in fireworks.items()]
