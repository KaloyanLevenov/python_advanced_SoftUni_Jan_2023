number_of_names = int(input())
set_of_names = {input() for _ in range(number_of_names)}
for name in set_of_names:
    print(name)
