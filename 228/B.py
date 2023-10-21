N,X = map(int,input().split())
A = list(map(int,input().split()))

seen = [0] * N

idx = X - 1
ans = 0
while True:
    if seen[idx] == 1:
        break
    seen[idx] = 1
    ans += 1
    idx = A[idx] - 1
print(ans)

