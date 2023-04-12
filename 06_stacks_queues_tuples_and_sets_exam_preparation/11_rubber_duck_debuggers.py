from collections import deque

time_list = deque(map(int, input().split()))
task_list = deque(map(int, input().split()))

register = {
    range(0, 61): 'Darth Vader Ducky',
    range(61, 121): 'Thor Ducky',
    range(121, 181): 'Big Blue Rubber Ducky',
    range(181, 241): 'Small Yellow Rubber Ducky'
}
ducky_made = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0,
}
while time_list and task_list:
    time = time_list.popleft()
    task = task_list.pop()
    total = time * task
    if total > 240:
        task_list.append(task - 2)
        time_list.append(time)

    for key, ducky in register.items():
        if total in key:
            ducky_made[ducky] += 1
            break

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f"{key}: {value}") for key, value in ducky_made.items()]