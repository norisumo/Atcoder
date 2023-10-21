N = int(input())
d = {}
for i in range(N):
    n,h = input().split()
    H = int(h)
    d[H] = n


ans = ""
d_s = sorted(d.items(), key=lambda x:x[0])

cnt = 0
for h,n in reversed(d_s):
    if cnt == 1:
        ans = n
        break
    cnt += 1

print(ans)