from sys import setrecursionlimit
setrecursionlimit(10**7)
N = int(input())
A = [[0] * 2*N for _ in range(2*N)]
for h in range(2*N-1):
    tmp = list(map(int,input().split()))
    for w in range(h+1,2*N):
        A[h][w] = tmp[w-h-1]
print(A)
ans = 0
def dfs(s,t):
    global ans
    seen = []
    unseen = []
    for i in range(2*N):
        if (s>>i) & 1:
            seen.append(i)
        else:
            unseen.append(i)
    if unseen == []:
        ans = max(t,ans)
        return
    unseen.sort()
    x = unseen[0]
    for y in unseen[1:]:
        dfs(s|(1<<x)|(1<<y),t^A[x][y])
 
dfs(0,0)
print(ans)