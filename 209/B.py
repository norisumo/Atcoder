N,X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    a = A[i]
    if (i+1)%2 == 0:
        a -= 1
    X -= a
if X >= 0:
    print("Yes")
else:
    print("No")


