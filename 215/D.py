N,M = map(int, input().split())
A = list(map(int,input().split()))

d = [1] * (M+1)
d[0] = -1
d[1] = -1
for i in range(2,M+1):
    if i**2 > M:
        break
    for j in range(i*2,M+1,i):
        d[j] = -1

s = set()
t = set()
for i in range(1,M+1):
    if d[i] > 0:
        s.add(i)
for i in range(N):
    a = A[i]
    while a % 2 == 0:
        t.add(2)
        a //=2
    f = 3
    while f**2 <= a:
        if a % f == 0:
            t.add(f)
            a //= f
        else:
            f += 2
    if a != 1:
        t.add(a)

for k in t:
    if k in s:
        s.remove(k)

s.add(1)
sl = list(s)
l = len(sl)
sl.sort()
print(l)
for i in range(l):
    print(sl[i])

