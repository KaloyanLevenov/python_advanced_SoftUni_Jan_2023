from collections import deque
from datetime import datetime, timedelta

#   ROB-15;SS2-10;NX8000-3  here we create dictionary where first we split every robot by ";", then
# we split every robot by "-" in order to take its name, factory time and the additional 0 is standing for the
# availability of the robot. If it os 0 means it is free if is equal to factory time or less means the robot
# is working and this is the remaining time
robots = {robot.split("-")[0]: [int(robot.split("-")[1]), 0] for robot in input().split(";")}
factory_time = datetime.strptime(input(), '%H:%M:%S')
products = deque()
item = input()

while item != "End":
    products.append(item)
    item = input()

while products:
    factory_time += timedelta(0,1)  # here we increase the time by 1 second. Zero stands for days, 1 stands for seconds
    current_product = products.popleft()

    robots = {robot[0]: [robot[1][0], robot[1][1] - 1] if robot[1][1] != 0 else robot[1] for robot in robots.items()}
    free_robots = list(filter(lambda x: x[1][1] == 0, robots.items()))

    if not free_robots:
        products.append(current_product)
        continue

    robots[free_robots[0][0]][1] = free_robots[0][1][0]

    print(f"{free_robots[0][0]} - {current_product} [{factory_time.strftime('%H:%M:%S')}]")
