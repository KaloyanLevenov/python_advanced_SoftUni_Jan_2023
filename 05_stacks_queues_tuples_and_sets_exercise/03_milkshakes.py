from collections import deque

chocolates = deque(int(x) for x in input().split(', '))  # starting from the last chocolate
cups_of_milk = deque(int(x) for x in input().split(', '))  # matching with the first cup of milk

milkshakes = 0

while milkshakes != 5 and chocolates and cups_of_milk:
    current_chocolate = chocolates.pop()
    current_cup_of_milk = cups_of_milk.popleft()
    if current_chocolate <= 0 and current_cup_of_milk <= 0:
        continue
    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_cup_of_milk)  # returning back the cup milk > 0 back to original position and loop again
        continue
    elif current_cup_of_milk <= 0:
        chocolates.append(
            current_chocolate)  # returning back the chocolate > 0 back to original position in stack and loop again
        continue

    if current_chocolate == current_cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milk.append(current_cup_of_milk)
        chocolates.append(current_chocolate - 5)


print("Great! You made all the chocolate milkshakes needed!") if milkshakes == 5 else print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")

