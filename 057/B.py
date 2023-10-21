import bisect

N,M = map(int,input().split())
s = []
for i in range(N):
    s.append(list(map(int,input().split())))
ms = []
for i in range(N):
    x = s[i][0]
    y = s[i][1]
    ms.append([(x+y),(x-y)])

c = []
for i in range(M):
    c.append(list(map(int,input().split())))

mc = []
for i in range(M):
    x = c[i][0]
    y = c[i][1]
    mc.append([(x+y),(x-y)])


INF = 1 << 60
for i in range(N):
    md = ms[i]
    check = INF
    ans = 0
    xs = ms[i][0]
    ys = ms[i][1]
    for j in range(M):
        xc = mc[j][0]
        yc = mc[j][1]
        md = max(abs(xs-xc), abs(ys-yc))
        if check > md:
            ans = j + 1
            check = md
    print(ans)
