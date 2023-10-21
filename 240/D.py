from collections import deque

N = int(input())
A = list(map(int, input().split()))
q = deque()
n = 1
q.append([A[0],n])
print(n)
for i in range(1,N):
    a = A[i]
    t,now = 0,0
    if q:
        t,now = q.pop()
    n += 1
    if a == t:
        if now + 1 == a:
            n -= a
        else:
            q.append([a, now+1])
    else:
        q.append([t,now])
        q.append([a,1])
    print(n)

