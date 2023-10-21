N,K = map(int,input().split())
A = list(map(int,input().split()))

KL = [[] for i in range(N)]

for i in range(0,K):
    for j in range(i,N,K):
        KL[i].append(A[j])
for i in range(K):
    KL[i].sort()


a = 0
for i in range(N):
    s = i % K
    t = i // K

    b = KL[s][t]
    if a > b:
        exit(print("No"))
    a = b

print("Yes")