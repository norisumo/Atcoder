from heapq import heappop, heappush

def dijkstra(s):
    d = [INF] * N
    d[s] = 0
    seen = [0] * N
    hq = [(0,s)]
    while hq:
        t, v = heappop(hq)
        seen[v] = 1
        if t <= d[v]:
            for to, co in adj[v]:
                if seen[to] == 0 and d[to] > t + co:
                    d[to] = t + co
                    heappush(hq, (d[to], to))
    return d


N,M = map(int,input().split())
INF = 1 << 60

adj = [[] for _ in range(N)]
loop = [INF] * N

for i in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    if a == b:
        loop[a] = min(loop[a], c)
    else:
        adj[a].append([b,c])




dist = []
for i in range(N):
    dist.append(dijkstra(i))

for i in range(N):
    ans = loop[i]
    for j in range(N):
        if i != j:
            ans = min(ans, dist[i][j] + dist[j][i])
    if ans >= INF:
        ans = -1
    print(ans)