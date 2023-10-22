import sys
sys.setrecursionlimit(10**8)

H,W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))


def dfs(i,j,s):
    cnt = 0
    if (i==H-1) and (j==W-1):
        cnt = 1
        return cnt
    if (i < H-1):
        n = A[i+1][j]
        if not n in s:
            s.add(n)
            cnt += dfs(i+1, j, s)
            s.remove(n)
    if (j < W-1):
        n = A[i][j+1]
        if not n in s:
            s.add(n)
            cnt += dfs(i, j+1, s)
            s.remove(n)
    return cnt 

ans = dfs(0,0,set([A[0][0]]))
print(ans)