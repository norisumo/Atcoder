N,M = map(int,input().split())
INF= 1 << 60

dp = [[INF] * N for i in range(N)]
dist = [[0] * N for i in range(N)]

for i in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    dp[a][b] = c
    dp[b][a] = c
    dist[a][b] = c

# ワーシャルフロイドで最短距離を算出
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
ans = 0
# スタート地点(s)とゴール地点(t)を決め、
# 中継地点(k)を全探索してs-tの辺を削除可能かチェックする。
for s in range(N):
    for t in range(s+1,N):
        for k in range(N):
            if dist[s][t] >= (dp[s][k] + dp[k][t]):
                ans += 1
                break

print(ans)
