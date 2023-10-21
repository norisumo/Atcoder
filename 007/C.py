from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

R,C = map(int,input().split())
sy,sx =map(int,input().split())
sy -= 1
sx -= 1

gy,gx =map(int,input().split())
gy -= 1
gx -= 1

c = []
for i in range(R):
    c.append(input())

INF = 1 << 60
dist = [[INF] * C for i in range(R)]
q = deque()
q.append([sy,sx])
dist[sy][sx] = 0

while q:
    t = q.popleft()
    y = t[0]
    x = t[1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if dist[ny][nx] != INF:
            continue
        if not(0 <= ny < R):
            continue
        if not(0 <= nx < C):
            continue
        if c[ny][nx] == '#':
            continue
        dist[ny][nx] = dist[y][x] + 1
        q.append([ny,nx])
ans = dist[gy][gx]
print(ans)

