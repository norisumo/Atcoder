H,W,K = map(int,input().split())
sx,sy,tx,ty = map(int,input().split())

# 方針：
# dpで考える。dp[k][i][j] = k回動かしてx2行目にいるか:i, y2列目にいるか:j
# しかし、上記のdpを愚直に行っていくと計算量が爆発し、到底間に合わずTLEする
# ⇒ goalのあるx2行目,y2列目以外は特に区別する必要はない。
#    dp[i][j]のi,jを0,1(x2,y2と同じ行または列かどうか)とし、k回繰り返す。
#    dpの値を一時保存するList Pを用意し、ループの最後でdpを更新してやることでdpを3次元から2次元にすることが出来、
# 　 大幅に計算量を抑えることができる。
# 遷移について：
# 例えば行の遷移を考えると・・・
#    i ⇒　0 → 0 = H-2(今いる行と目的の行以外)
#    　  　0 → 1 = 1 (今いる行から目的の行への遷移)
#    　  　1 → 0 = H-1 (今いる行が目的の行であり、目的行以外への遷移)
#    　  　1 → 1 = 0 (今いる行が目的の行であるので、目的行への遷移はできない。)

mod = 998244353
dp = [[0] * 2 for i in range(2)]
dp[sx == tx][sy == ty] = 1

for ki in range(K):
    p = [[0] * 2 for i in range(2)]
    for j in range(2):
        p[0][j] = (p[0][j] + dp[0][j] * (H-2) % mod) % mod
        p[1][j] = (p[1][j] + dp[0][j]) % mod
        p[0][j] = (p[0][j] + dp[1][j] * (H-1) % mod) % mod

    for i in range(2):
        p[i][0] = (p[i][0] + dp[i][0] * (W-2) % mod) % mod
        p[i][1] = (p[i][1] + dp[i][0]) % mod
        p[i][0] = (p[i][0] + dp[i][1] * (W-1) % mod) % mod
    dp = p

print(dp[1][1] % mod)