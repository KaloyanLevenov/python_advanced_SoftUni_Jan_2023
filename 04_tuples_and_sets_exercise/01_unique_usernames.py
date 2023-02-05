number_of_names = int(input())
set_of_names = {input() for _ in range(number_of_names)}
print(*set_of_names,sep='\n')