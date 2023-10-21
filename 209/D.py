import sys
sys.setrecursionlimit(10**7)

N,Q = map(int, input().split())
INF = 1 << 60
t = [set() for i in range(N)]
d = [INF] * N 
for i in range(N-1):
    a,b= map(int, input().split())
    a -= 1
    b -= 1
    t[a].add(b)
    t[b].add(a)


def dfs(x):
    #今いる町からいける町へ移動する
    for nt in t[x]:
        #すでに探索済みの町が来たら0をreturn
        if d[nt] != INF:
            continue
        d[nt] = d[x] + 1
        dfs(nt)
    return True
d[0] = 0
dfs(0)

for q in range(Q):
    c,dd = map(int, input().split())
    c -= 1
    dd -= 1
    ans = d[c] + d[dd]
    if ans % 2 == 1:
        print("Road")
    else:
        print("Town")



