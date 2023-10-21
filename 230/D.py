N,D = map(int,input().split())

t = []
for i in range(N):
    l,r = map(int,input().split())
    t.append([r,l])

t.sort()

sd = 0
ed = 0
ans = 0

for i in range(N):
    r,l = t[i]
    if r < sd or ed < l:
        sd = r
        ed = r + D - 1
        ans += 1

print(ans)