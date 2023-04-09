def start_spring(**kwargs):
    register = dict()
    for name, type in kwargs.items():
        if type not in register.keys():
            register[type] = []
        register[type].append(name)

    register = dict(sorted(register.items(), key=lambda x: (-len(x[1]), x[0])))
    [value.sort() for value in register.values()]
    result = []
    for key, value in register.items():
        result.append(f"{key}:")
        result.extend(f"-{object}" for object in value)
    return '\n'.join(result)

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
