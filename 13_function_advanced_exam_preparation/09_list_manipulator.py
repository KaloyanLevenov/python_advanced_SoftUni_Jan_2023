def list_manipulator(*args):
    number_list, action, addition, *rest = args

    def add_func(argument):
        nonlocal number_list
        if argument == "beginning":
            number_list = rest + number_list
        elif argument == "end":
            number_list.extend(rest)

    def remove_func(argument):
        nonlocal number_list
        if argument == "beginning":

            if not rest:
                number_list.pop(0)
            else:
                for _ in range(rest[0]):
                    number_list.pop(0)

        elif argument == "end":

            if not rest:
                number_list.pop()
            else:
                for _ in range(rest[0]):
                    number_list.pop()

    if action == 'add':
        add_func(addition)
    elif action == 'remove':
        remove_func(addition)

    return number_list