from heapq import heappop, heappush
from collections import defaultdict

N = int(input())
S = input()
W = list(map(int,input().split()))
d = defaultdict(list)

num = 0

for i in range(N):
    s = S[i]
    if s == '1':
        num += 1
    d[W[i]].append(i)

sW = set(sorted(W))
ans = num
for w in sW:
    for idx in d[w]:
        if S[idx] == '1':
            num -= 1
        else:
            num += 1
    ans = max(num,ans)

print(ans)