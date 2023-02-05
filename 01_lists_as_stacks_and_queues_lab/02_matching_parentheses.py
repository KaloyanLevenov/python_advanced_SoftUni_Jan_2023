string = input()
stack = []
for index in range(len(string)):
    char = string[index]
    if char == "(":
        stack.append(index)
    elif char == ")":
        closing_char = index
        opening_char = stack.pop()
        print(string[opening_char:closing_char + 1])
