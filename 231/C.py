import bisect

N,Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
for _ in range(Q):
    x = int(input())
    i = bisect.bisect_left(A,x)
    ans = N - i
    print(ans)




