register = {}
list_of_numbers = [float(number) for number in input().split()]
while list_of_numbers:
    current_number = list_of_numbers.pop(0)
    if current_number not in register.keys():
        register[current_number] = 0
    register[current_number] += 1

for number, occurrences in register.items():
    print(f"{number:.1f} - {occurrences} times")

