def grocery_store(**kwargs):
    receipt = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    receipt = [f'{name}: {quantity}' for name, quantity in receipt]
    return '\n'.join(receipt)


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))