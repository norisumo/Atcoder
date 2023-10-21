N = int(input())
A = list(map(int,input().split()))

m = [0] * (10**5 + 2)
ma = max(A)
la = len(A)
for i in range(la):
    a = A[i]
    m[a] += 1
    na = a + 1
    m[na] += 1
    ba = a - 1
    m[ba] += 1

ans = 0
cnt = 0
for i in range(ma+1):
    ca = m[i]
    if ca > cnt:
        ans = i
        cnt = ca
print(cnt)

