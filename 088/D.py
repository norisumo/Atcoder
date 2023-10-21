from collections import deque

dy = [-1,0,1,0]
dx = [0,-1,0,1]

H,W = map(int,input().split())
s = []
b_num = 0
for i in range(H):
    s.append(input())
    for j in range(W):
        if s[i][j] == '#':
            b_num += 1
INF = 1 << 60
dist = [[INF] * W for i in range(H)]
dist[0][0] = 1
q = deque()
q.append([0,0])

while q:
    y,x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if not(0 <= ny < H):
            continue
        if not(0 <= nx < W):
            continue
        if dist[ny][nx] != INF:
            continue
        if s[ny][nx] == "#":
            continue
        dist[ny][nx] = dist[y][x] + 1
        q.append([ny,nx])

ans = dist[H-1][W-1]
if ans == INF:
    ans = -1
    exit(print(ans))
ans = H * W - ans -b_num
print(ans)



