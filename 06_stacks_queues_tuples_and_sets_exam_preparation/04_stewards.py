from collections import deque

seats = set(input().split(', '))
seats_taken = []
first_number_sequence = deque(map(int, input().split(', ')))
second_number_sequence = deque(int(x) for x in input().split(', '))

rotation = 0

for _ in range(10):
    if len(seats_taken) == 3:
        break

    current_number_one = first_number_sequence.popleft()
    current_number_two = second_number_sequence.pop()
    total = current_number_one + current_number_two
    ascii_char = chr(total)
    combo_one = str(current_number_one) + ascii_char
    combo_two = str(current_number_two) + ascii_char

    if combo_one in seats or combo_two in seats:
        if combo_one in seats:
            seats_taken.append(combo_one)
        else:
            seats_taken.append(combo_two)
        seats.difference_update(seats_taken)
    else:
        first_number_sequence.append(current_number_one)
        second_number_sequence.appendleft(current_number_two)

    rotation += 1

print(f"Seat matches: {', '.join(seats_taken)}")
print(f"Rotations count: {rotation}")
