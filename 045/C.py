S = input()
sl = []
l = 0
for s in S:
    sl.append(int(s))
    l += 1

l2 = 1 << (l-1)
ans = 0
for i in range(l2):
    now = sl[0]
    for j in range(l-1):
        idx = j + 1
        if i & (0x01 << j):
            ans += now
            now = sl[idx]
        else:
            now = now * 10 + sl[idx]
    ans += now


print(ans)

