H,W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))
for i in range(W):
    for j in range(H):
        print(A[j][i], end = " ")
    print("")