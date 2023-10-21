
A = list(map(int, input().split()))
A.sort(reverse=True)

ans = A[0] + A[1]
print(ans)