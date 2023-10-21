from collections import deque
from bisect import bisect, bisect_left

N,K = map(int,input().split())
P = list(map(int,input().split()))

ans = [-1] * N
cnt = [0] * N
iL = [-1] * N
qL = [deque() for i in range(N)]
s = set()

X = P[0]
s.add(X)
xi = X-1
cnt[xi] = 1
iL[xi] = 0
qL[0].appendleft(X)


for i in range(1,N):
    X = P[i]
    xi = X - 1
    ni = bisect_left(list(s),X)
    




