def set_creation(scope):
    first_number, second_number = scope.split(',')
    return {number for number in range(int(first_number), int(second_number) + 1)}


def intersection_check(set_one, set_two, biggest_intersection):
    current_intersection = set_one.intersection(set_two)
    if len(current_intersection) > len(biggest_intersection):
        return current_intersection
    else:
        return biggest_intersection


longest_intersection = {}
number_of_lines = int(input())
for _ in range(number_of_lines):
    first_range, second_range = input().split('-')
    first_set = set_creation(first_range)
    second_set = set_creation(second_range)
    longest_intersection = intersection_check(first_set,second_set,longest_intersection)

print(f'Longest intersection is {sorted(longest_intersection)} with length {len(longest_intersection)}')


# Second Solution
#longest_intersection = set()

#for _ in range(int(input())):
#    first_data, second_data = [el.split(",") for el in input().split("-")]

#    first_range = set(range(int(first_data[0]), int(first_data[1]) + 1))
 #   second_range = set(range(int(second_data[0]), int(second_data[1]) + 1))

  #  intersection = first_range.intersection(second_range)

   # if len(longest_intersection) < len(intersection):
    #    longest_intersection = intersection

#print(
 #   f"Longest intersection is "
  #  f"[{', '.join(str(x) for x in longest_intersection)}] "
   # f"with length {len(longest_intersection)}"
#)