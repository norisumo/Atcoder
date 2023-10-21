from collections import deque

N = 9
M = int(input())
to = [[] for i in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)


P = list(map(int,input().split()))
start = ["9"] * N
for i in range(N-1):
    p = P[i] - 1
    start[p] = str(i+1)


# 目標状態：iが頂点iにある
goal = [str(i+1) for i in range(N)]




# 状態と距離を辞書で保持する
dist = {}
q = deque()
seen = set()
q.append((start, 0))
INF = 1 << 60
ans = INF
while q:
    now, d = q.popleft()
    empty = now.index("9")
    if now == goal:
        ans = d
        break
    for u in to[empty]:
        tmp = now[u]
        nowtmp = now[:]
        nowtmp[u] = "9"
        nowtmp[empty] = tmp
        now_str = "".join(nowtmp)
        if not(now_str in seen):
            seen.add(now_str)
            q.append((nowtmp, d+1))
        

if ans == INF:
    print(-1)
else:
    print(ans)
