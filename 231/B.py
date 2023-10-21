N = int(input())
d = {}
for i in range(N):
    s = input()
    if not(s in d):
        d[s] = 1
    else:
        d[s] += 1

dd = sorted(d.items(), key=lambda x:x[1])

ans = dd[-1][0]

print(ans)