from heapq import heappush, heappop

N,M = map(int, input().split())
to = [[] for i in range(N)]
# 入次数のカウンタ
deg = [0] * N


for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    deg[b] += 1

# heapq
q = []

# 入次数0をheapqに入れる
for i in range(N):
    if deg[i] == 0:
        heappush(q, i)

T = []
while q:
    if len(q) >= 2:
        exit(print("No"))
    v = heappop(q)
    T.append(v+1)
    for u in to[v]:
        deg[u] -= 1
        if deg[u] == 0:
            heappush(q, u)
    

if len(T) != N:
    print("No")
    exit()
ans = [0] * N
for i in range(N):
    t = T[i]
    ans[t-1] = i+1

print("Yes")
print(*ans)
