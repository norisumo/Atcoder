import sys
sys.setrecursionlimit(10**7)

N,Q = map(int,input().split())
t = [set() for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    t[a].add(b)
    t[b].add(a)

memo = [0] * N
for i in range(Q):
    p,x = map(int,input().split())
    p -= 1
    memo[p] += x

INF = 1 << 60
a = [INF] * N

def dfs(x, p = -1):
    if a[x] != INF:
        return
    if p < 0:
        a[x] = memo[x]
    else:
        a[x] = a[p] + memo[x]
    for s in t[x]:
        dfs(s,x)


dfs(0)
for i in range(N):
    print(a[i], end=" ")



