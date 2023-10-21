N,X = map(int,input().split())
INF = 1 << 60
ans = INF
now = 0
for i in range(N):
    a,b = map(int,input().split())
    if X - i - 1 < 0:
        break
    now = now + a + b
    ans = min(ans, now + b * (X-i-1))
print(ans)

