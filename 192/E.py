from heapq import heappop, heappush

N,M,X,Y = map(int,input().split())
X -= 1
Y -= 1
adj = [[] for i in range(N)]
INF = 1 << 60

for i in range(M):
    a,b,t,k = map(int,input().split())
    a -= 1
    b -= 1
    adj[a].append([b,t,k])    
    adj[b].append([a,t,k])


def dijkstra(s):
    d = [INF] * N
    seen = [0] * N
    hq = [(0,s)]
    d[s] = 0
    while hq:
        t,v = heappop(hq)
        if seen[v] == 1:
            continue
        if d[v] < t:
            continue
        seen[v] = 1
        for nex,nt,k in adj[v]:
            c = 0
            if t % k != 0:
                c = k - d[v] % k
            tt = d[v] + nt + c
            if seen[nex] == 0 and tt < d[nex]:
                d[nex] = tt
                heappush(hq, (tt,nex))
    return d


cost = dijkstra(X)

ans = cost[Y]
if ans == INF:
    ans = -1
print(ans)