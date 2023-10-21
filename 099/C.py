N = int(input())
INF = 1 << 60
dp = [INF] * (N+1)
dp[0] = 0


for n in range(1,N+1):
    p = 0
    while (6 ** p) <= n:
        t = 6**p
        dp[n] = min(dp[n-t] + 1, dp[n])
        p += 1
    p = 0
    while (9 ** p) <= n:
        t = 9**p
        dp[n] = min(dp[n-t] + 1, dp[n])
        p += 1
ans = dp[N]
print(ans)