import collections
import sys
sys.setrecursionlimit(10**7)
import collections

N,X = map(int,input().split())
T = []
nums = []
for i in range(N):
    tmp = list(map(int,input().split()))
    nums.append(tmp[0])
    T.append(collections.Counter(tmp[1:]))

def dfs(v,n,idx):
    ret = 0
    nidx = idx + 1
    if nidx == N:
        if X == v:
            return n
        return 0
    for nv,nn in T[nidx].items():
        ret += dfs(v * nv, n * nn, nidx)
    return ret

ans = 0
for v,n in T[0].items():
    ans += dfs(v,n,0)

print(ans)