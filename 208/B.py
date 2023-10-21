import math

N = int(input())

ans = 0
for i in reversed(range(1,10+1)):
    p = math.perm(i)

    ans += N // p

    N = N % p

    if N == 0:
        break

print(ans)