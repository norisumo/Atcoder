N,K,A = map(int, input().split())

idx = A - 1
for i in range(K):
    idx = (idx + 1) % N
    
if idx == 0:
    idx = N


print(idx)