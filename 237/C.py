from collections import deque

S = list(input())

t = deque()

l = len(S)
flag = 1
cnt = 0
for i in reversed(range(l)):
    s = S[i]
    if s == 'a' and flag == 1:
        cnt += 1
        continue
    else:
        flag = 0
    t.appendleft(s)
    
flag = 1
c = 0
while t:
    ln = t.popleft()
    if not(t):
        break
    if ln == 'a' and flag == 1:
        c += 1
        if c > cnt:
            print("No")
            exit()
        continue
    else:
        flag = 0
    rn = t.pop()
    if rn != ln:
        print("No")
        exit()

print("Yes")