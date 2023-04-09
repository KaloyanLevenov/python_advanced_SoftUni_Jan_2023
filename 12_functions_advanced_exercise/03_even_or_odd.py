def even_odd(*args):
    action = args[-1]
    result = None
    if action == 'even':
        result = list(filter(lambda x: x % 2 == 0, args[:-1]))
    if action == 'odd':
        result = list(filter(lambda x: x % 2 == 1, args[:-1]))
    return result


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, "even"))
