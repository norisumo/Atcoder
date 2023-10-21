from bisect import bisect, bisect_left, bisect_right

N = int(input())
A = list(map(int,input().split()))

d = [[] for i in range(N+1)]
for i in range(N):
    d[A[i]].append(i+1)

Q = int(input())
for i in range(Q):
    l,r,x = map(int,input().split())
    ans = bisect_right(d[x], r) - bisect_right(d[x], l-1)
    print(ans)

