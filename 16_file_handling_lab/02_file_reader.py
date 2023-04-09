file = open('numbers.txt', 'r')
total = 0
for number in file:
    total += int(number)
print(total)