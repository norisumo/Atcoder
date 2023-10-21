from collections import defaultdict
from heapq import heappop, heappush
Q = int(input())
d = defaultdict(int)

maxq = []
minq = []

for i in range(Q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        x = que[1]
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
        if d[x] == 1:
            heappush(minq, x)
            heappush(maxq, -x)
    elif que[0] == 2:
        x = que[1]
        c = que[2]
        c = min(c, d[x])
        d[x] -= c
        if d[x] <= 0:
            if minq:
                t = heappop(minq)
                if t != x:
                    heappush(minq,t)
                else:
                    while minq:
                        n = heappop(minq)
                        if d[n] > 0:
                            heappush(minq,n)
                            break
            if maxq:
                t = heappop(maxq)
                if t != -x:
                    heappush(maxq,t)
                else:
                    while maxq:
                        n = heappop(maxq)
                        if d[-n] > 0:
                            heappush(maxq,n)
                            break

    elif que[0] == 3:
        s = -1 * heappop(maxq)
        l = heappop(minq)
        ans =  s - l
        heappush(maxq, -s)
        heappush(minq, l)
        print(ans)

