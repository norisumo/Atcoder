from collections import defaultdict
import itertools

N = int(input())
X = defaultdict(list)
Y = defaultdict(list)

for i in range(N):
    x,y = map(int,input().split())
    X[x].append(y)
    Y[y].append(x)

ans = 0
for x in X:
    t = list(itertools.combinations(X[x], 2))
    if t == []:
        continue
    for tt in t:
        ya = tt[0]
        yb = tt[1]
        for x2 in Y[ya]:
            if x2 <= x:
                continue
            if x2 in Y[yb]:
                ans += 1
                


print(ans)