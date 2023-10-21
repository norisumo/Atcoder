N,M,K = map(int, input().split())
dp = [[0] * (M+1) for i in range(N)]
mod = 998244353
dp[0][0] = 0
for i in range(M+1):
    dp[0][i] += dp[0][i-1] + 1
print(dp)
for i in range(1,N):
    for j in range(1,M+1):
        if 0 < j - K <= M:
            dp[i][j] += dp[i-1][j-K]
            dp[i][j] %= mod
        elif 0 < K - j <= M:
            dp[i][j] += dp[i-1][j-K]
            dp[i][j] %= mod
print(dp)
print(dp[N-1][M])