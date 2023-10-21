from collections import deque
import heapq

A = []
#heapq.heapify(A)
q = deque()
s = set()
Q = int(input())
for i in range(Q):
    query = list(map(int, input().split()))
    n = query[0]
    if n == 1:
        x = query[1]
        q.append(x)
    elif n == 2:
        if A != []:
            print(heapq.heappop(A))
        else:
            print(q.popleft())
            
    elif n == 3:
        while q:
            n = q.popleft()
            heapq.heappush(A, n)




