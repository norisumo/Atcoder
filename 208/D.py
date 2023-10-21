N,M = map(int,input().split())
INF = 1 << 60

dp = [[INF] * N for i in range(N+1)]

for i in range(N):
  dp[i][i] = 0

for i in range(M):
  a,b,c = map(int,input().split())
  a -= 1
  b -= 1
  dp[a][b] = c

ans = 0
for k in range(N):
  for i in range(N):
    for j in range(N):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
      if dp[i][j] != INF:
        ans += dp[i][j]
print(ans)