mod = 998244353

N,M,K = map(int,input().split())
dp = [[0] * (K+1) for i in range(N+1)]

for i in range(1,M+1):
    dp[1][i] = 1


for i in range(1,N+1):
    for j in range(1,K+1):
        for k in range(1,M+1):
            if 1 <= (j - k):
                dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % mod

ans = 0
for i in range(1,K+1):
    ans = (ans + dp[N][i]) % mod
print(ans)