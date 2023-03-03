first_set = {int(x) for x in input().split()}
second_set = {int(x) for x in input().split()}

for _ in range(int(input())):
    first_command, *data = input().split()
    command = first_command + ' ' + data.pop(0)
    if command == 'Add First':
        [first_set.add(int(number)) for number in data]
    elif command == 'Add Second':
        [second_set.add(int(number)) for number in data]
    elif command == 'Remove First':
        [first_set.remove(int(number)) for number in data if int(number) in first_set]
    elif command == 'Remove Second':
        [second_set.discard(int(number)) for number in data]
    else:
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print(True)
        else:
            print(False)

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
