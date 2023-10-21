N = int(input())

s = set()
for i in range(N):
    A = list(map(int, input().split()))
    l = A[0]
    s.add(tuple(A[1:]))
ans = len(s)
print(ans)