# 答えに単調性がある(4組まではOKで5組以降はNG、みたいな)ので
# 答えを二分探索することが可能

N,K = map(int,input().split())
A = list(map(int,input().split()))

# 二分探索の判定は、チェックしたい組数(wj)とA[i]のminを
# 取り、N個すべての和sを求める。
# それが、K * wj以上ならばTrue
# 例えば、K = 3, wj = 4、A = [7,3,5,1]のとき、minを取っているので
# 頭から並べた場合、同じものを2つ選ぶ選び方はできない。
# AAAA
# BBBC
# CCCD
# みたいな
def check(wj):
    s = 0
    for i in range(N):
        s += min(A[i], wj)
    if s >= K * wj:
        return True
    else:
        return False

ac = 0
wa = (3*10**17) // K
while wa - ac > 1:
    wj = (ac + wa) // 2
    if check(wj):
        ac = wj
    else:
        wa = wj

print(ac)

