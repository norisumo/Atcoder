from collections import deque

N,M = map(int,input().split())
INF = 1 << 60
dist = [INF] * N
cnt = [0] * N
road = [set() for i in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    road[a].add(b)
    road[b].add(a)

q = deque()
q.append(0)
dist[0] = 0
cnt[0] = 1
mod = 10**9 + 7
while q:
    now = q.popleft()
    for nex in road[now]:
        if dist[nex] == INF:
            dist[nex] = dist[now] + 1
            cnt[nex] = (cnt[nex] + cnt[now]) % mod
            q.append(nex)
        else:
            if dist[nex] == dist[now] + 1:
                cnt[nex] = (cnt[nex] + cnt[now]) % mod
ans = cnt[N-1] % mod
print(ans)
