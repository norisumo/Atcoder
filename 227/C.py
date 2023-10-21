import math
N = int(input())
ans = 0
t = []
c = 0
for a in range(1,N+1):
    if a ** 2 > N:
        break
    bc = N // a
    t.append([a,bc])
    c += 1

for i in range(c):
    a,bc = t[i]
    for b in range(a,bc+1):
        if b ** 2 > bc:
            break
        c = bc // b
        if c < b:
            break
        ans += (c - b + 1)


print(ans)