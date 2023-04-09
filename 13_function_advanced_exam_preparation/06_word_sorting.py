def words_sorting(*args):
    register = {word: sum(map(ord, word)) for word in args}

    value_total = sum([value for value in register.values()])
    register = dict(sorted(register.items(), key=lambda x: -x[1] if value_total % 2 == 1 else x[0]))
    result = [f"{key} - {value}" for key, value in register.items()]

    return '\n'.join(result)