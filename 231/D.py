import sys
sys.setrecursionlimit(10**7)
N,M = map(int, input().split())

t = [set() for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    t[a].add(b)
    t[b].add(a)

def dfs(r,n):
    seen[n] = 1
    ret = True
    for nex in t[n]:
        if nex == r:
            continue
        if seen[nex] == 1:
            ret = False
            break
        ret = dfs(n,nex)
    return ret
 

ans = "Yes"
seen = [0] * N
for i in range(N):
    seen[i] = 1
    if len(t[i]) > 2:
        exit(print("No"))
    for k in t[i]:
        if seen[k] == 1:
            continue
        if not dfs(i,k):
            exit(print("No"))


print(ans)