def stock_availability(*args):
    inventory_list, action, *rest = args

    if action == 'delivery':
        [inventory_list.append(stock) for stock in rest] if rest else None

    elif action == 'sell':
        if rest:
            if len(rest) == 1 and isinstance(rest[0], int):
                number = rest[0]
                [inventory_list.pop(0) for _ in range(number)]

            elif all(x.isalpha() for x in rest):
                while rest:
                    last_param = rest.pop()
                    [inventory_list.remove(item) if item == last_param else None for item in inventory_list.copy()] if last_param in inventory_list else None
        else:
            inventory_list.pop(0)

    return inventory_list