import collections

N,K = map(int,input().split())
A = list(map(int,input().split()))
s = [0] * (N+1)

for i in range(N):
    idx = i + 1
    s[idx] = s[i] + A[i]

C = collections.Counter(s)
ans = 0
for i in range(N):
    n = K + s[i]
    C[s[i]] -= 1
    if n in C:
        ans += C[n]
    
print(ans)