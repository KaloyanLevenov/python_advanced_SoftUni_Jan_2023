def func_executor(*args):
    function_data = args
    result = [f"{func.__name__} - {func(*arguments)}" for func, arguments in function_data]
    return '\n'.join(result)


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
