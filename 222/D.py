N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
mod = 998244353

M = 3001
dp = [0] * M
dp[0] = 1
for i in range(N):
    p = [0] * M
    for j in range(M-1):
        dp[j+1] = (dp[j+1] + dp[j]) % mod
    
    for j in range(M):
        if A[i] <= j <= B[i]:
            p[j] = (p[j] + dp[j]) % mod
    dp = p

ans = 0
for i in range(M):
    ans = (ans + dp[i]) % mod

print(ans)