N = int(input())
A = list(map(int, input().split()))
X = int(input())

t = [0] * (N)
for i in range(N):
    if i > 0:
        t[i] = t[i-1] + A[i]
    else:
        t[i] = A[i]

s = t[N-1]

j = X // s
k = X % s
g = 0
for i in range(N):
    if k < t[i]:
        g = i + 1
        break
ans = j*N + g
print(ans)

