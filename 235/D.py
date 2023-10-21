from collections import deque

a,N = map(int, input().split())
q = deque()
q.append(1)
M = 10 ** 6 + 1
INF = 1 << 60
dist = [INF] * (M)
dist[1] = 0
while q:
    x = q.popleft()
   # print("x:",x)
    sx = str(x)
    nx = x * a
    nd = dist[x]
    if nx < M:
        if dist[nx] > nd + 1:
            if N == nx:
                exit(print(nd + 1))
                break
            else:
                dist[nx] = nd + 1
                q.append(nx)
    if x % 10 == 0:
        continue

    nnx = (int)(sx[-1] + sx[:-1])
    if nnx < M:
        if dist[nnx] > nd + 1:
            if N == nnx:
                exit(print(nd + 1))
            else:
                dist[nnx] = nd + 1
                q.append(nnx)
    

print(-1)




