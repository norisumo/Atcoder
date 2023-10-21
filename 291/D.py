N = int(input())
dp = [[0] * 2 for i in range(N+1)]
dp[1][0] = 1
dp[1][1] = 1
mod = 998244353
C = [[] for i in range(N+1)]
for i in range(N):
    a,b = map(int, input().split())
    C[i+1] = [a,b]
for i in range(2,N+1):
    if (C[i][0] != C[i-1][0]):
        dp[i][0] += dp[i-1][0]
        dp[i][0] %= mod
    if (C[i][0] != C[i-1][1]):
        dp[i][0] += dp[i-1][1]
        dp[i][0] %= mod
    if (C[i][1] != C[i-1][0]):
        dp[i][1] += dp[i-1][0]
        dp[i][1] %= mod
    if (C[i][1] != C[i-1][1]):
        dp[i][1] += dp[i-1][1]
        dp[i][1] %= mod
    
ans = dp[N][0] + dp[N][1]
print(ans%mod)
