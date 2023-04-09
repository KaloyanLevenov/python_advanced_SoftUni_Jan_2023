def rectangle(length, width):
    if type(width) != int or type(length) != int:
        return "Enter valid values!"

    if length <= 0 or width <= 0:
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return length * 2 + width * 2

    return f'''Rectangle area: {area()}
Rectangle perimeter: {perimeter()}'''


print(rectangle(5,10))
