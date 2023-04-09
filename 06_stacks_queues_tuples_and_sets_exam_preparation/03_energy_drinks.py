from collections import deque

CAFFEINE_LIMIT = 300
caffeine = list(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))
stamat_caffeine = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_drink = energy_drinks.popleft()
    total = current_drink * current_caffeine
    if stamat_caffeine + total <= 300:
        stamat_caffeine += total
    else:
        energy_drinks.append(current_drink)
        stamat_caffeine = (stamat_caffeine - 30) if stamat_caffeine >= 30 else 0

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")
