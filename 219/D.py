N = int(input())
X,Y = map(int,input().split())
INF = 1 << 60
dp = [[[INF] * (Y+1) for i in range(X+1)] for j in range(N+1)]
dp[0][0][0] = 0
for i in range(1,N+1):
    idx = i-1
    a,b = map(int,input().split())
    for j in range(X+1):
        for k in range(Y+1):
            dp[i][min(j+a, X)][min(k+b, Y)] = min(dp[i][min(j+a, X)][min(k+b, Y)], dp[i-1][j][k] + 1)

            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])



ans = dp[N][X][Y]
if ans == INF:
    ans = -1
print(ans)