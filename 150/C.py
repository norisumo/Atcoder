import itertools
N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

t = list(itertools.permutations((range(1,N+1))))
a = 0
b = 0
l = len(t)
print(t)
for i in range(l):
    if t[i] == P:
        a = i
    if t[i] == Q:
        b = i

ans = abs(a-b)
print(ans)
