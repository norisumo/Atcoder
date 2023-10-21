A = list(map(int, input().split()))

ans = "Yes"

A.sort()
if A[2] - A[1] == A[1] - A[0]:
    ans = "Yes"
else:
    ans = "No"


print(ans)