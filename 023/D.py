N = int(input())
H = []
S = []
for i in range(N):
    h,s = map(int,input().split())
    H.append(h)
    S.append(s)

INF = 1 << 60
ac = INF
wa = 0
while ac - wa > 1:
    m = (ac + wa) // 2

    t = [0] * N
    isOK = True
    for i in range(N):
        if m < H[i]:
            isOK = False
        else:
            t[i] = (m - H[i]) // S[i]
    t.sort()

    for i in range(N):
        if t[i] < i:
            isOK = False
    if isOK:
        ac = m
    else:
        wa = m
print(ac)

