from collections import defaultdict
import itertools
import math

p = []
N,K = map(int, input().split())

if K == 1:
    exit(print("Infinity"))

for i in range(N):
    x,y = map(int, input().split())
    p.append([x,y])

d = defaultdict(tuple)


def calc(s,t):
    x1,y1,x2,y2 = s[0],s[1],t[0],t[1]
    dx = x1 - x2
    dy = y1 - y2
    if dx < 0:
        dx = -dx
        dy = -dy
    a = 0
    b = 0
    if dx == 0:
        a = 0
        b = 1
    else:
        g = math.gcd(dx,dy)
        a = dx // g
        b = dy // g
    
    c = a * y1 - b * x1

    if not (a,b,c) in d:
        d[a,b,c] = 1
    else:
        d[a,b,c] += 1



for a,b in itertools.combinations(p,2):
    calc(a,b)

ans = 0
m = K * (K-1) // 2
for k,v in d.items():
    if v >= m:
        ans += 1
print(ans)
