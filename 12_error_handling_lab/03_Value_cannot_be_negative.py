class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    try:
        number = int(input())
        if number < 0:
            raise ValueCannotBeNegative('Value can not be negative number.')
    except ValueCannotBeNegative as text:
        print(text)

