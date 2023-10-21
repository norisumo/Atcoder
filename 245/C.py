N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0]*2 for i in range(N)]
dp[0][0] = 1
dp[0][1] = 1
for i in range(1,N):
    if dp[i-1][0] == 1:
        if abs(A[i] - A[i-1]) <= K:
            dp[i][0] = 1
        if abs(B[i] - A[i-1]) <= K:
            dp[i][1] = 1
    if dp[i-1][1] == 1:
        if abs(A[i] - B[i-1]) <= K:
            dp[i][0] = 1
        if abs(B[i] - B[i-1]) <= K:
            dp[i][1] = 1

if dp[N-1][0] == 1 or dp[N-1][1] == 1:
    print("Yes")
else:
    print("No")
