N = int(input())
T = list(map(int,input().split()))

tot = 0
dp = 1
for i in range(N):
    t = T[i]
    dp |= dp << t
    tot += t

ans = 1 << 60
for i in range(tot):
    if (dp >> i) & 0x01:
        ans = min(ans, max(i, tot - i))

print(ans)
