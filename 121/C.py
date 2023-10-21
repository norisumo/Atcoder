N,M = map(int,input().split())
d = []
for i in range(N):
    a,b = map(int,input().split())
    d.append([a,b])
d.sort()

ans = 0
for i in range(N):
    a,b = d[i]
    if b >= M:
        ans += M * a
        break
    else:
        ans += b * a
        M -= b
print(ans)

