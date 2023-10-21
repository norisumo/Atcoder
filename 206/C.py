import collections
import math
import collections
N = int(input())
A = list(map(int, input().split()))
ans = 0
s = collections.Counter([A[0]])
c = 1
for i in range(1,N):
    t = A[i]
    if s[t]:
        ans += (i-s[t])
        s[t] += 1
    else:
        ans += i
        s[t] = 1


print(ans)

