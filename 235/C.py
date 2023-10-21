from collections import defaultdict
import enum

N,Q = map(int,input().split())
A = list(map(int,input().split()))

d = defaultdict(list)

for i ,x in enumerate(A,1):
    d[x].append(i)

for i in range(Q):
    x,k = map(int,input().split())
    if k <= len(d[x]):
        print(d[x][k-1])
    else:
        print(-1)

