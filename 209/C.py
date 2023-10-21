import math
N = int(input())
C = list(map(int, input().split()))
mod = 10**9 + 7

mc = max(C)
C.sort()
ans = 1
n = 0
t = 0
for i in range(N):
    c = C[i]
    if i == 0:
        n = c
        t = n
    elif n == c:
        t -= 1
    else:
        t = t + (c-n) - 1
        n = c
    ans = ans * t % mod
print(ans % mod)
