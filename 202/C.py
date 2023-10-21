N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

bb = []
for i in range(N):
    c = C[i] - 1
    bb.append(B[c])
d = [0] * (N+1)

for i in range(N):
    a = A[i]
    d[a] += 1

ans = 0
for i in range(N):
    b = bb[i]
    ans += d[b]
print(ans)
