import itertools

N,M = map(int,input().split())
T = [[0] * N for i in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    T[a][b] = 1
    T[b][a] = 1

A = [[0] * N for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    A[a][b] = 1
    A[b][a] = 1

for cL in itertools.permutations(range(N)):
    flag = True
    for i in range(N):
        ni = cL[i]
        for j in range(N):
            nj = cL[j]
            if T[ni][nj] != A[i][j]:
                flag = False
                break
    if flag:
        exit(print("Yes"))

print("No")
