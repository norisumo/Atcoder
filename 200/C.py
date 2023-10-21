import math
N = int(input())
A = list(map(int, input().split()))

mod = 200

t = [0] * mod 
for i in range(N):
    a = A[i] % mod
    t[a] += 1

ans = 0
for i in range(mod):
    a = t[i]
    if a > 1:
        ans += math.comb(a,2)
print(ans)
   

