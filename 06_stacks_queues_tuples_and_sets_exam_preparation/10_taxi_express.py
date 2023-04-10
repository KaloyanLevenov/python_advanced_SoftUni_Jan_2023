from collections import deque

customer_list = deque(map(int, input().split(', ')))
taxi_list = list(map(int, input().split(', ')))
total_time = 0

while customer_list:
    if not taxi_list:
        print("Not all customers were driven to their destinations")
        print(f'Customers left: {", ".join(str(x) for x in customer_list)}')
        break

    customer = customer_list.popleft()  # first customer to last taxi
    taxi = taxi_list.pop()

    if taxi >= customer:
        total_time += customer
    else:
        customer_list.appendleft(customer)

else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")