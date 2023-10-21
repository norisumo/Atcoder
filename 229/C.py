N,W = map(int,input().split())

C = []

for i in range(N):
    a,b = map(int,input().split())
    C.append([a,b])

C.sort(reverse=True)

w = 0
d = 0
for i in range(N):
    a,b = C[i]
    if b <= W:
        d += (a * b)
        W -= b
    else:
        d += (a * W)
        break
print(d)
