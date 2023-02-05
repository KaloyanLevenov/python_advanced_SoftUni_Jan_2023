from collections import deque

water_in_dispenser = int(input())
people = deque()
COMMAND_START = 'Start'
COMMAND_END = 'End'
COMMAND_REFILL = 'refill'
names = input()
while names != COMMAND_START:
    people.append(names)
    names = input()

command = input()
while command != COMMAND_END:

    if command.isnumeric():
        liters = int(command)
        if liters <= water_in_dispenser:
            print(f"{people.popleft()} got water")
            water_in_dispenser -= liters
        else:
            print(f"{people.popleft()} must wait")

    elif COMMAND_REFILL in command:
        command_list = command.split()
        refill_liters = int(command_list[1])
        water_in_dispenser += refill_liters

    command = input()
print(f"{water_in_dispenser} liters left")