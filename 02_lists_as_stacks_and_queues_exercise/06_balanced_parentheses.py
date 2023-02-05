from collections import deque

parenthesis = deque(input())
opened_parenthesis = deque()

while parenthesis:
    current_symbol = parenthesis.popleft()
    if current_symbol in "({[":
        opened_parenthesis.append(current_symbol)
    elif not opened_parenthesis:
        print("NO")
        break
    else:
        if f"{opened_parenthesis.pop() + current_symbol}" not in "()[]{}":
            print("NO")
            break
else:
    print("YES")