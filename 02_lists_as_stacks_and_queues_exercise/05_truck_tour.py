from collections import deque

number_of_pumps = int(input())
# comprehension with which for every pump I enter the information for it
petrol_pumps = deque([[int(x) for x in input().split()] for _ in range(number_of_pumps)])
# this copy is needed to work on the queue and dynamically edit it
petrol_pumps_copy = petrol_pumps.copy()
index = 0
gas_in_tank = 0

while petrol_pumps_copy:
    petrol, distance = petrol_pumps_copy.popleft()
    gas_in_tank += petrol
    if gas_in_tank - distance < 0:
        petrol_pumps.rotate(-1)
        gas_in_tank = 0
        # we work on queue_copy, but in the end we are changing its data to queue.coppy()
        petrol_pumps_copy = petrol_pumps.copy()
        index += 1
    else:
        gas_in_tank -= distance

print(index)
