import sys
from collections import deque
green_window = int(input())
free_window = int(input())
cars = deque()
total_cars_passed = 0
command = input()
while command != 'END':
    if command != 'green':
        cars.append(command)
    else:
        current_green = green_window

        while current_green > 0 and cars:
            current_car = cars.popleft()
            full_time = current_green + free_window

            if len(current_car) > full_time:
                print(f"A crash happened!\n{current_car} was hit at {current_car[full_time]}.")
                sys.exit()

            current_green -= len(current_car)
            total_cars_passed += 1

    command = input()

print(f'Everyone is safe.\n{total_cars_passed} total cars passed the crossroads.')

