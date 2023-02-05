from collections import deque

COMMAND_GREEN = 'green'
crash_happened = False
total_cars_passed = 0
cross_road = []
cars = deque()
green_window = input()
green_window_copy = int(green_window)
free_window = input()
free_window_copy = int(free_window)
command = input()
while command != "END":
    if command != COMMAND_GREEN:
        car = command
        cars.append(car)
    elif command == COMMAND_GREEN:
        total_cars_passed = 0
        while (green_window_copy or free_window_copy) and cars:
            current_car = cars.popleft()
            if green_window_copy - len(current_car) > 0:
                total_cars_passed += 1
                green_window_copy -= len(current_car)
            else:
                time_rest = green_window_copy + free_window_copy
                if len(current_car) > time_rest:
                    cross_road.append(current_car[:time_rest])
                    print("A crash happened!")
                    print(f"{current_car} was hit at {current_car[time_rest]}.")
                    crash_happened = True
                    break

                elif len(crrent_car) <= time_rest:
                    time_rest -= len(current_car)
                    total_cars_passed += 1


    if crash_happened:
        break
    cross_road.clear()
    green_window_copy = int(green_window)
    free_window_copy = int(free_window)

    command = input()
else:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")
