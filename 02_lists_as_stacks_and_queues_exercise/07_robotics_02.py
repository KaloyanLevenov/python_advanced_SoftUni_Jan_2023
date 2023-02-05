from collections import deque
from datetime import datetime, timedelta

robots = {}

# robots = {robot.split("-")[0]: [int(robot.split("-")[1]), 0] for robot in input().split(";")}
for robot in input().split(";"):
    name, time_needed = robot.split("-")
    robots[name] = [int(time_needed), 0]

factory_time = datetime.strptime(input(), '%H:%M:%S')
products = deque()
item = input()

while item != "End":
    products.append(item)
    item = input()

while products:
    factory_time += timedelta(0, 1)  # here we increase the time by 1 second. Zero stands for days, 1 stands for seconds
    current_product = products.popleft()

    free_robots = []
    for robot in robots.items():
        # ('ROB', [15, 0]) example for robot in robots.items()
        if robot[1][1] > 0:
            robot[1][1] -= 1
    for robot in robots.items():
        if robot[1][1] == 0:
            free_robots.append(robot)

    if not free_robots:
        products.append(current_product)
        continue

    robot_name, data = free_robots[0]
    robots[robot_name][1] = data[0]

    print(f"{free_robots[0][0]} - {current_product} [{factory_time.strftime('%H:%M:%S')}]")
