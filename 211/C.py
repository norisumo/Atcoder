import bisect

S = input()

cL = [[] for i in range(8)]

l = len(S)
for i in range(l):
    s = S[i]
    if s == 'c':
        cL[0].append(i)
    elif s == 'h':
        cL[1].append(i)
    elif s == 'o':
        cL[2].append(i)
    elif s == 'k':
        cL[3].append(i)
    elif s == 'u':
        cL[4].append(i)
    elif s == 'd':
        cL[5].append(i)
    elif s == 'a':
        cL[6].append(i)
    elif s == 'i':
        cL[7].append(i)

c_length = [0] * 8
for i in range(8):
    cl = len(cL[i])
    c_length[i] = cl

ans = 0
mod = 10 ** 9 + 7
for i in range(8):
    













