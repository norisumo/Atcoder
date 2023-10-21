s = input()
m = []
a = []
for i in range(10):
    if s[i] == 'o':
        m.append(i)
    elif s[i] == '?':
        a.append(i)
ans = 0
lm = len(m)
for i in range(10000):
    S = str(i).zfill(4)
    cnt  = 0
    used = [0] * 10
    ng = False
    for j in m:
        if not str(j) in S:
            ng = True
            break
        for s in S:
            if str(j) == s:
                cnt += 1
    if ng:
        continue
    for j in a:
        for s in S:
            if str(j) == s:
                cnt += 1
    if cnt == 4:
            ans += 1
print(ans)