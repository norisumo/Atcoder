import sys
sys.setrecursionlimit(10**7)

N = int(input())
T =[]
K = []
W = []
for i in range(N):
    A = list(map(int,input().split()))
    T.append(A[0])
    K.append(A[1])
    W.append(A[2:])

n = N-1
seen = [0] * N
def dfs(x):
    if seen[x] == 1:
        return 0
    retTime = T[x]
    seen[x] = 1
    for i in range(K[x]):
        nx = W[x][i] - 1
        retTime += dfs(nx)
    return retTime




ans = dfs(n)
print(ans)

