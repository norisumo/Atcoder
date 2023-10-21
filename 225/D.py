from collections import deque


N,Q = map(int, input().split())
INF = 1 << 60
t = [[INF,INF] for i in range(N)]
for i in range(Q):
    q = input().split()
    c = int(q[0])
    if c == 1:
        x = int(q[1])
        y = int(q[2])
        x -= 1
        y -= 1
        t[x][1] = y
        t[y][0] = x

    elif c == 2:
        x = int(q[1])
        y = int(q[2])
        x -= 1
        y -= 1
        t[x][1] = INF
        t[y][0] = INF
    elif c == 3:
        x = int(q[1])
        x -= 1
        q = deque()
        q.append(x+1)
        b,a = t[x]
        while 1:
            if b == INF:
                break
            q.appendleft(b+1)
            b = t[b][0]
            
        while 1:
            if a == INF:
                break
            q.append(a+1)
            a = t[a][1]
            
        ans = list(q)
        l = len(ans)
        print(l, end=" ")
        print(*ans)






