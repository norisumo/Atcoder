N = int(input())
A = [[] for i in range(30)]
A[0] = [1,1]
print(1)
if N == 1:
    exit()
print(*A[0])
for i in range(1,N-1):
    for j in range(len(A[i-1])+1):
        if j== 0 or j == len(A[i-1]):
            A[i].append(1)
        else:
            A[i].append(A[i-1][j-1] + A[i-1][j])
    print(*A[i])



