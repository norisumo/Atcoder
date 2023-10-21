# コストに負の辺が出てくるのでそのままダイクストラは使えない。
# x->yに対して登る時のコスト-2*(Hy-Hx)に対して、2倍を考えなければ -> Hx - Hyと書き換えられる。
# 1 -> 2 -> 3 -> 4と進むとき、(H1 - H2) + (H2 - H3) + (H3 - H4) = (H1 - H4)
# つまり始点と終点の差になる。
# それでは一旦無視していた2倍を考えると始点と終点の差に上った高さ分引くと求めたい答えになる。
# つまり、登った高さのコスト計算には負辺が出てこず、ダイクストラを使えばよい
from heapq import heappop, heappush

N,M = map(int, input().split())
H = list(map(int, input().split()))

road = [set() for i in range(N)]

for i in range(M):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    road[u].add(v)
    road[v].add(u)

INF = 1 << 60
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
        for to in road[v]:
            co = max(0, H[to] - H[v])
            if (seen[to] == 0) and (co + t < dist[to]):
                dist[to] = t + co
                heappush(hq, (dist[to], to))
    return dist


ans = 0
d = dijkstra(0)
for i in range(1,N):
    now = H[0] - H[i] - d[i]
    ans = max(ans, now)
print(ans)