N,M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

rA = list(reversed(A))
rC = list(reversed(C))
rans = [0] * (M+1)

for i in range(M+1):
    if rA[0] == 0:
        n = 0
    else:
        n = rC[i] // rA[0]
    rans[i] = n
    for j in range(1,N+1):
        rC[i+j] -= n * rA[j]


ans = list(reversed(rans))
print(*ans)
