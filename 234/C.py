from collections import deque

K = int(input())
t = format(K, 'b')

l = len(t)
ans = deque()
for i in reversed(range(l)):
    n = t[i]
    if n == '1':
        n = '2'
    ans.append(n)

for i in range(l):
    a = ans.pop()
    print(a,end="")



print("")