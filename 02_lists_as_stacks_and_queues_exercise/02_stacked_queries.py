stack = []
commands_dict = {1: lambda x: stack.append(x[1]),
                 2: lambda x: stack.pop() if len(stack) > 0 else None,
                 3: lambda x: print(max(stack)) if len(stack) > 0 else None,
                 4: lambda x: print(min(stack)) if len(stack) > 0 else None,
                 }
number = int(input())
for _ in range(number):
    command = [int(x) for x in input().split()]
    commands_dict[command[0]](command)  # command[0] stands for the key in command_dict
    # and to be sure we have no errors if we have command 1 we have 2 elements in command
    # however we have only the key in the 2nd, 3rd and 4th command so as argument of the lambda function we put the hole
    # command=[], so if we don't have additional argument we are not going to crash the code.
stack.reverse()
print(*stack, sep= ', ')
