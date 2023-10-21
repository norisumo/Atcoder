
N,P = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for i in range(N):
    if A[i] < P:
        ans += 1

print(ans)