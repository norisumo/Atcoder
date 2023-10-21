import bisect

N,M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

ans = 1 << 60
for i in range(N):
    a = A[i]
    idx = bisect.bisect(B,a)
    if idx == M:
        ans = min(ans, abs(a-B[idx-1]))
    elif B[idx] == a:
        ans = 0
        break
    elif idx == 0:
        ans = min(ans, abs(a-B[idx]))
    else:
        bt = abs(a-B[idx-1])
        at = abs(a-B[idx])
        ans = min(ans,bt,at)
print(ans)


