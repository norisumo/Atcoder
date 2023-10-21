from collections import deque

X = input()
l = len(X)
q = deque()
s = 0
nex = 0
for i in range(l):
    s += int(X[i])

for i in reversed(range(l)):
    t = X[i]
    n = (s + nex) % 10

    q.appendleft(n)
    nex = (s + nex) // 10
    s -= int(t)
    
if nex > 0:
    q.appendleft(nex)

while q:
    ans = q.popleft()
    print(ans, end = "")
print("")