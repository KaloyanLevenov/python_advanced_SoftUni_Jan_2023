from collections import deque


def food_is_enough(needed_food, available_food):
    if needed_food > available_food:
        return False
    else:
        return True


food_availability = int(input())
orders = deque(int(x) for x in input().split())
biggest_order = max(orders)

print(biggest_order)

while orders:
    current_order = orders.popleft()
    if food_is_enough(current_order, food_availability):
        food_availability -= current_order
    else:
        orders.appendleft(current_order)
        print(f'Orders left: {" ".join(str(i) for i in orders)}')
        break
else:
    print("Orders complete")

