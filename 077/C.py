import bisect

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort()
B.sort()
C.sort()


ans = 0
for i in range(N):
    b = B[i]
    a = bisect.bisect_left(A,b)
    if A[a] == b:
        a -= 1
    c = bisect.bisect_right(C,b)
    if c < N and C[c] == b:
        c -= 1
    c = N - c
    ans += (a*c)
print(ans)
