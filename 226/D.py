import itertools
import math

N = int(input())
Z = []
for i in range(N):
    Z.append(list(map(int, input().split())))

all = list(itertools.combinations((range(N)), 2))
l = len(all)
a = set()

for i in range(l):
    s,t = all[i]
    x1,y1 = Z[s]
    x2,y2 = Z[t]
    dx = x1 - x2
    dy = y1 - y2
    g = math.gcd(dx,dy)
    dx = dx // g
    dy = dy // g

    a.add((dx,dy))
    a.add((-dx,-dy))
ans = len(a)
print(ans)