import collections

N,K = map(int, input().split())
A = list(map(int, input().split()))

c = collections.Counter(A[:K])
ans = len(c)
t = ans
for i in range(K,N):
    a = A[i]
    b = A[i-K]
    if c[a] == 0:
        t += 1
    c[a] += 1
    c[b] -= 1
    if c[b] == 0:
        t -= 1
    ans = max(ans,t)
    
        
    
    

print(ans)

