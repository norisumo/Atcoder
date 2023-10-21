from collections import deque

N,X = map(int, input().split())
S = input()
n = 0
q = deque()
for i in reversed(range(N)):
    if S[i] == 'U':
        n += 1
    else:
        if n != 0:
            n -= 1
            continue
        else:
            q.appendleft(S[i])

if n != 0:
    for i in range(n):
        X //= 2

while q:
    t = q.popleft()
    if t == 'L':
        X *= 2
    else:
        X = X*2 + 1


print(X)