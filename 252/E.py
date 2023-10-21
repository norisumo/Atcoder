from heapq import heappop, heappush
from collections import defaultdict

N,M = map(int,input().split())
adj = [[] for i in range(N)]

for i in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    n = i + 1
    adj[a].append([c,b,n])
    adj[b].append([c,a,n])

INF = 1 << 60
dl = defaultdict(int)
def dijkstra(s):
    dist = [INF] * N
    seen = [0] * N
    dist[s] = 0
    hq = [(0,s)]
    while hq:
        t,v = heappop(hq)
        seen[v] = 1
        if dist[v] < t:
            continue
        for co, to, roadNo in adj[v]:
            if (seen[to] == 0) and (co + t < dist[to]):
                dist[to] = t + co
                dl[to] = roadNo
                heappush(hq, (dist[to], to))
    return dist



ds = dijkstra(0)

ans = []
for road in dl.values():
    ans.append(road)

print(*ans)


