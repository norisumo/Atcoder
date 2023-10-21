N,K = map(int, input().split())
n = N
a = list(map(int, input().split()))
A = []
for i in range(N):
    A.append([a[i],i])
A.sort()
a = [0] * N
t = K // N
n = K % N
nn = n
for i in reversed(range(n)):
    a[i] += 1
    n -= 1

ans = []
for i in range(N):
    ans.append([A[i][1], a[i]])

ans.sort()
for i in range(N):
    print(t + ans[i][1])



