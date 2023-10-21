N = int(input())
T = []
for i in range(N):
    a,b = map(int, input().split())
    T.append([a,b])

t = 0
for i in range(N):
    a,b = T[i]
    t += (a / b)

bt = t / 2
ans = 0
for i in range(N):
    a,b = T[i]
    nt = a / b
    if 0 < bt <= nt:
        ans += (bt * b)
        break
    else:
        ans += a
        bt -= nt
print(ans)