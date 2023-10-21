from heapq import heappop, heappush

N,M = map(int,input().split())
hq = []
d = [0] * N
to = [[] for i in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    d[b] += 1
    to[a].append(b)

for i in range(N):
    if d[i] == 0:
        heappush(hq,i)

ans = []

while hq:
    v = heappop(hq)
    ans.append(v+1)
    for u in to[v]:
        d[u] -= 1
        if d[u] == 0:
            heappush(hq,u)

if len(ans) != N:
    print(-1)
else:
    print(*ans)


