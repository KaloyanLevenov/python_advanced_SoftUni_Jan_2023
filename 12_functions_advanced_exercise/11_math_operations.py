from collections import deque
math_register = {
    'a': lambda x, y: x + y,
    's': lambda x, y: x - y,
    'd': lambda x, y: x / y,
    'm': lambda x, y: x * y,
}


def math_operations(*args, **kwargs):
    numbers = list(args)
    operations = deque(kwargs)

    for index in range(len(numbers)):
        operator = operations.popleft()

        if not operations:
            operations += kwargs
        number = numbers[index]

        if number == 0 and operator == 'd':
            continue

        kwargs[operator] = math_register[operator](kwargs[operator], number)

    result = []

    for key, value in sorted(kwargs.items(), key= lambda x: (-x[1], x[0])):
        result.append(f"{key}: {value:.1f}")

    return '\n'.join(result)

