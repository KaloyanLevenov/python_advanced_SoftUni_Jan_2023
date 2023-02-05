def parking_lot(command, number, register):
    if command == COMMAND_IN:
        register.add(number)
    if command == COMMAND_OUT:
        register.discard(number)



def print_func(register):
    if not register:
        print("Parking Lot is Empty")
    else:
        for number in register:
            print(number)


register = set()
COMMAND_IN = 'IN'
COMMAND_OUT = 'OUT'
number_of_commands = int(input())
for _ in range(number_of_commands):
    direction, car_number = input().split(", ")
    parking_lot(direction,car_number,register)
print_func(register)
