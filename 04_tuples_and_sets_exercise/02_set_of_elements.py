n,m = input().split()
n_set = {input() for _ in range(int(n))}
m_set = {input() for _ in range(int(m))}
output = n_set.intersection(m_set)
print(*output,sep='\n')
