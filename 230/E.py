N = int(input())

now = 1
ans = 0
while now <= N:
    X = N // now
    nex = N // X + 1
    ans += (nex - now) * X
    now = nex
print(ans)
