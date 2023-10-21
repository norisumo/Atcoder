N = int(input())
A = list(map(int,input().split()))
now = 0
s = set()
s.add(360)
for a in A:
    now = (now + a) % 360
    s.add(now)

ans = 0
t = 0
sl = list(s)
sl.sort()
for n in sl:
    ans = max(ans,n-t)
    t = n

print(ans)

