mod = 10 ** 9 + 7
MAX_N = 3005

dp = [[0] * MAX_N for i in range(MAX_N)]

ds = [[0] * MAX_N for i in range(MAX_N)]
N = int(input())
A = list(map(int, input().split()))

s = [0] * (N+1)
for i in range(N):
    s[i+1] = s[i] + A[i]

#iは0スタート
dp[0][1] = 1
#mod 1 で0になるところに1を初期化
ds[1][0] = 1
for i in range(1,N+1):
    #dsを更新しながら処理していきたいので、jを大きい順に更新していく(i=1で更新したところが影響してくる)
    for j in range(i,0,-1):
        now = 0
        #dsにはmod j でkになるものを持っておく
        now = ds[j][s[i]%j]
        dp[i][j+1] = now
        ds[j+1][s[i]%(j+1)] = (ds[j+1][s[i]%(j+1)] + now) % mod
    '''
    for j in range(1,i+1):
        #高速化する
        for k in range(i):
            if ((s[i]-s[k])%j == 0):
                now += dp[k][j]
        dp[i][j+1] = now
    '''
        #dp[i][j+1]へ遷移してくる(もらう)dp
        #dp[i][j+1] = 
ans = 0

for j in range(1,N+2):
    ans += dp[N][j]
    ans %= mod
print(ans)