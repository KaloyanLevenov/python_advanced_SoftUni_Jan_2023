from functools import reduce

expression = input().split()
left_index = 0
right_index = 0
functions = {
    '*': lambda i, k: reduce(lambda a, b: a * b, map(int, expression[i:k])),
    '/': lambda i, k: reduce(lambda a, b: a // b, map(int, expression[i:k])),
    '+': lambda i, k: reduce(lambda a, b: a + b, map(int, expression[i:k ])),
    '-': lambda i, k: reduce(lambda a, b: a - b, map(int, expression[i:k])),

}

while right_index < len(expression):
    current_element = expression[right_index]
    if current_element in '/*-+':
        result = functions[current_element](left_index,right_index)
        expression[right_index] = result
        left_index = right_index
    right_index += 1

print(result)