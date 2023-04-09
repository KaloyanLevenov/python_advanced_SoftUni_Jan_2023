from collections import deque

bowls_of_ramen = deque(map(int, input().split(', ')))
customers = deque(map(int, input().split(', ')))

while bowls_of_ramen and customers:
    bowl = bowls_of_ramen.pop()
    customer = customers.popleft()

    if bowl == customer:
        continue
    elif bowl > customer:
        bowls_of_ramen.append(bowl - customer)
    elif customer > bowl:
        customers.appendleft(customer - bowl)

if not customers:  # means there are no customers in the queue and they all are served.
    print("Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join(map(str, bowls_of_ramen))}") if bowls_of_ramen else None
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")