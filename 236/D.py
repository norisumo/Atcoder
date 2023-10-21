import sys
sys.setrecursionlimit(10**7)

N = int(input())
n2 = N * 2
a = [[0] * n2 for i in range(n2)]

for i in range(n2-1):
    t = list(map(int, input().split()))
    idx = 0
    for j in range(i+1,n2):
        a[i][j] = t[idx]
        a[j][i] = t[idx]
        idx += 1

def dfs(s, x):
    si = -1
    global ans
    for i in range(n2):
        if not(s[i]):
            si = i
            break

    if si == -1:
        ans = max(ans,x)
        return
    
    s[si] = 1
    for i in range(n2):
        if not(s[i]) and (si != i):
            s[i] = 1
            dfs(s, x^a[si][i])
            s[i] = 0
    s[si] = 0

s = [0] * n2
ans = 0
dfs(s,0)
print(ans)
