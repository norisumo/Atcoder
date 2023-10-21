import heapq


N,K = map(int, input().split())
P = list(map(int, input().split()))

t = []
for i in range(K):
    heapq.heappush(t, P[i])

ans = heapq.heappop(t)
print(ans)
heapq.heappush(t, ans)

for i in range(K,N):
    n = heapq.heappop(t)
    m = P[i]
    x = max(n,m)
    heapq.heappush(t, x)
    ans = heapq.heappop(t)
    print(ans)
    heapq.heappush(t, ans)
