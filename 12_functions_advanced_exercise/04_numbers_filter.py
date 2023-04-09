def even_odd_filter(**kwargs):
    register = dict()

    for name, list_of_numbers in kwargs.items():

        if name == 'even':
            if name not in register.keys():
                register[name] = []
            register[name] += list(filter(lambda x: x % 2 == 0, list_of_numbers))

        elif name == 'odd':
            if name not in register.keys():
                register[name] = []
            register[name] += list(filter(lambda x: x % 2 == 1, list_of_numbers))

    return dict(sorted(register.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5]))
