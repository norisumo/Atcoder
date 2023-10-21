S = input()
T = input()
l = len(S)
base = ord('a')
M = 26
for n in range(M):
    flag = True
    for i in range(l):
        c = chr((ord(S[i]) - base + n) % M + base)
        if c != T[i]:
            flag = False
            break
    if flag:
        exit(print("Yes"))

print("No")


