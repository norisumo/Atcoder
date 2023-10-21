N,X = map(int, input().split())
t = []
for i in range(N):
    t.append(list(map(int,input().split())))
dp = [[0] * (X+1) for i in range(N+1)]
dp[0][0] = 1
for i in range(N):
    a ,b = t[i]
    for j in range(X+1):
        if a + j <= X:
            dp[i+1][j+a] += dp[i][j]

        if b + j <= X:
            dp[i+1][j+b] += dp[i][j]

t = dp[N][X]
if t != 0:
    print("Yes")
else:
    print("No")
