from collections import deque

N = int(input())
s = list(input())
q = deque()
q.append(N)
for i in reversed(range(N)):
    if s[i] == 'R':
        q.appendleft(i)
    else:
        q.append(i)

while q:
    ans = q.popleft()
    print(ans, end = " ")