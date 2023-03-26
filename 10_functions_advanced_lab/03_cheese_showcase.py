def sorting_cheeses(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    output = []
    for name, quantity in kwargs:
        output.extend([name, *sorted(quantity, reverse=True)])

    return '\n'.join(str(x) for x in output)