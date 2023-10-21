from collections import Counter

N = int(input())
A = list(map(int,input().split()))
C = Counter(A)

M = max(A)
ans = 0
for a,v in C.items():
    for b in range(1,M//a + 1):
        c = a * b
        ans += C[a] * C[b] * C[c]


print(ans)


