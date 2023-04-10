def numbers_searching(*args):
    duplicate = {x for x in args if args.count(x) > 1}  # set of duplicate numbers in args
    lowest_number = min(args)
    biggest_number = max(args)
    scope = range(lowest_number, biggest_number)
    missing_number = (set(scope).difference(args))
    result = [*[x for x in missing_number], [x for x in sorted(duplicate)]]
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
