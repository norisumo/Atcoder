N,K = map(int,input().split())
L = (K**2) // 2 + 1

A = []
for i in range(N):
    A.append(list(map(int,input().split())))

# mより大きい時に1、m以下の時は0とする。
# K*Kの区画無いの1が初めてL以下になった時のmが求めたい
# (L以上の時は常に中央値がmより大きいため)
ac = 1 << 60
wa = -1
while ac - wa > 1:
    m = (ac + wa) // 2

    ok = False
    s = [[0] * (N+1) for i in range(N+1)]

    #横方向の累積和を求める
    for i in range(N):
        for j in range(N):
            t = 0

            if A[i][j] > m:
                t = 1
            else:
                t = 0
            s[i+1][j+1] = s[i+1][j] + t

    #縦方向の累積和を求める
    for i in range(N):
        for j in range(N):
            s[i+1][j+1] += s[i][j+1]


    for i in range(N-K+1):
        for j in range(N-K+1):
            cnt = s[i+K][j+K]
            cnt -= s[i+K][j]
            cnt -= s[i][j+K]
            cnt += s[i][j]

            if cnt < L:
                ok = True

    if ok:
        
        ac = m
    else:
        wa = m
print(ac)


