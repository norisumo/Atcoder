# 解説動画その1
# f(N,D) = 高さNの完全2分木内の距離Dの個数
# f(4,3) = f(3,3) * 2 + g(4,3) (<= 値を使うケース)
# g(4,3) = g(3,3) + (葉を使うパス)
mod = 998244353

N,D = map(int,input().split())
two = [0] * (N+1)
two[0] = 1
for i in range(N):
    two[i+1] = (two[i]*2) % mod

ans = 0
f = [0] * (N+1)
g = [0] * (N+1)

# １～Nまで
for i in range(1,N+1):
    # 左のパスの長さ l
    l = i - 1
    # 右のパスの長さ r = D-l
    r = D-l
    # 葉の数
    leaf = 0

    # gを求める
    # rは0 <= r <= i-1
    if ((0 <= r) and (r <= i-1)):
        # 親が根の時、本当は0だが、-1になってしまうため、maxを取る
        leaf = (two[max(l-1,0)] * two[max(r-1,0)]) % mod
        # 基本的に左右対称なので2倍するが、左右両方とも葉を用いるケースは2倍するとかぶってカウントしてしまうので除く
        if l != r:
            leaf = (leaf * 2) % mod
    g[i] = (g[i-1] + leaf) % mod

    # fを求める
    for i in range(1,N+1):
        f[i] = ((f[i-1] * 2) % mod + g[i]) % mod

ans = (f[N] * 2) % mod
print(ans)
