N,A,X,Y = map(int, input().split())
ans = 0
if N < A:
    ans = N * X
else:
    ans = A * X + (N-A) * Y
print(ans)

