def name_func(name_list):
    the_odd_set = set()
    the_even_set = set()

    for name in name_list:
        total = 0
        counter = name_list.index(name) + 1
        for char in name:
            total += ord(char)
        total //= counter
    #the same thing for row 5-10
    #for row in range(1, int(input()) + 1):
        #ascii_sum_of_name = sum(ord(l) for l in input()) // row

        if total % 2 == 0:
            the_even_set.add(total)
        else:
            the_odd_set.add(total)
    return the_odd_set, the_even_set


def print_func(the_odd_set, the_even_set):
    odd_set_sum = sum(the_odd_set)
    even_set_sum = sum(the_even_set)
    if odd_set_sum == even_set_sum:
        print(*the_odd_set.union(even_set), sep=', ')
    elif odd_set_sum > even_set_sum:
        print(*the_odd_set.difference(even_set), sep=', ')
    elif odd_set_sum < even_set_sum:
        print(*the_odd_set.symmetric_difference(the_even_set), sep=', ')


names = [input() for _ in range(int(input()))]
odd_set, even_set = name_func(names)
print_func(odd_set, even_set)
