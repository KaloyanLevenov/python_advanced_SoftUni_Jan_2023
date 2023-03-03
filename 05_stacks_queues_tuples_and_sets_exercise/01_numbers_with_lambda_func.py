first_set = {int(x) for x in input().split()}
second_set = {int(x) for x in input().split()}
functions = {
    'Add First': lambda x: [first_set.add(number) for number in x],
    'Add Second': lambda x: [second_set.add(number) for number in x],
    'Remove First': lambda x: [first_set.remove(number) for number in x if number in first_set],
    'Remove Second': lambda x: [second_set.discard(number) for number in x],
    'Check Subset': lambda: print(True) if first_set.issubset(second_set) or second_set.issubset(first_set) else print(
        False),

}

for _ in range(int(input())):
    first_command, *data = input().split()
    command = first_command + ' ' + data.pop(0)
    if data:
        functions[command]([int(number) for number in data])
    else:
        functions[command]()

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
