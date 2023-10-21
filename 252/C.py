from collections import defaultdict
from collections import Counter

N = int(input())
d = defaultdict(list)

for i in range(N):
    S = input()
    for j in range(10):
        i_s = int(S[j])
        d[i_s].append(j)

     
ans = 1 << 60
for i in range(10):
    c = Counter(d[i])
    t = 0
    for i,n in c.items():
        t = max(t,i+10*(n-1))
    ans = min(ans,t)

print(ans)