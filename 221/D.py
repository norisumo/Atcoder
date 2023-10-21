N = int(input())
t = []

for i in range(N):
    a,b = map(int, input().split())
    t.append([a,1])
    t.append([a+b,-1])

ans = 0
t.sort()
lt = len(t)
now = 0
old = 0
tt = 0
p = [0] * (N+1)
for i in range(lt):
    d, c = t[i]
    if d == old:
        if now > 0:
            p[now] -= tt
    else:
        tt = d - old
    p[now] += tt
    now += c
    old = d

p[now] += tt        

for i in range(1,N+1):
    print(p[i], end = " ")

print("")