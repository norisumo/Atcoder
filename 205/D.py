import bisect

N,Q = map(int, input().split())
A = list(map(int, input().split()))

for i in range(Q):
    k = int(input())
    t = k
    while 1:
        r = bisect.bisect_left(A,t)
        if r >= N:
            t = k + r
            break
        if A[r] == t:
            r += 1
        t = k + r
        c = bisect.bisect_left(A,t)
        if c <= r and (c >= N or A[c] != t):
            break          
    print(t)
