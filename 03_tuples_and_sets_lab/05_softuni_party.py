number_of_guests = int(input())
invited_guests = set(input() for _ in range(number_of_guests))
arrived_guests = set()
command = input()

while command != "END":
    guest = command
    arrived_guests.add(guest)
    command = input()

absent_guests = sorted(list(invited_guests.difference(arrived_guests)))
print(len(absent_guests), sep='\n', *absent_guests)
