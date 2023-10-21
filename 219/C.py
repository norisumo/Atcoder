X = input()
N = int(input())

c = [0] * 26
ca = ord('a')
sl = []

for i in range(26):
    cx = ord(X[i])
    xid = cx - ca
    c[xid] = i

for i in range(N):
    S = input()
    t = ""
    for s in S:
        cs = ord(s)
        sid = cs - ca
        t += str(chr(c[sid] + ca))
    sl.append([t, S])

sl.sort()
for i in range(N):
    print(sl[i][1])

