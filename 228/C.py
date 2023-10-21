N,K = map(int,input().split())
P = []
for i in range(N):
    p1,p2,p3 = map(int,input().split())
    s = p1 + p2 + p3
    P.append([s,i])

P.sort(reverse=True)
INF = 1 << 60
A = [[] for i in range(N)]
b = INF
for i in range(N):
    s,idx = P[i]
    if i < K:
        A[idx] = "Yes"
        if i == K-1:
            b = s
    elif s + 300 >= b:
        A[idx] = "Yes"
    else:
        A[idx] = "No" 

for i in range(N):
    print(A[i])


