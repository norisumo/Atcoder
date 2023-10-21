N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    n = A[i]
    if n <= ans:
        break
    ans = n

print(ans)