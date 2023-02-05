text = input()
register_of_occurrences = {}
for character in text:
    if character not in register_of_occurrences.keys():
        register_of_occurrences[character] = 0
    register_of_occurrences[character] += 1
sorted_register_of_occurrences = sorted(register_of_occurrences.items(), key = lambda x: x[0])
for elements in sorted_register_of_occurrences:
    symbol, occurrences = elements
    print(f"{symbol}: {occurrences} time/s")