from collections import deque

Q = int(input())
q = deque()

for i in range(Q):
    S = list(map(int,input().split()))
    if S[0] == 1:
        q.append([S[1],S[2]])
    elif S[0] == 2:
        c = S[1]
        ans = 0
        while c > 0:
            x,n = q.popleft()
            if n > c:
                ans += c * x
                n -= c
                c = 0
                q.appendleft([x,n])
            elif n == c:
                ans += c * x
                c = 0
            else:
                ans += n * x
                c -= n
        print(ans)


