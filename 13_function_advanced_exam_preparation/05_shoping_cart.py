def shopping_cart(*arguments):
    menu = {
        'Soup': [],
        'Pizza': [],
        'Dessert': [],
    }
    limit = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2,
    }

    for argument in arguments:

        if argument == 'Stop':
            break
        else:
            meal, product = argument

        if (product not in menu[meal]) and (len(menu[meal]) < limit[meal]):
            menu[meal].append(product)

    menu = dict(sorted(menu.items(), key=lambda x: (-len(x[1]), x[0])))
    [products.sort() for products in menu.values()]
    no_products = not any(menu.values())
    result = []
    if no_products:
        result.append("No products in the cart!")
    else:
        for meal, products in menu.items():
            result.append(f"{meal}:")
            if products:
                result.extend([f" - {product}" for product in products])

    return '\n'.join(result)