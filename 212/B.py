s = input()
mod = 10

if s[0] == s[1] == s[2] == s[3]:
    exit(print("Weak"))

next = int(s[0])
isOk = True
for i in range(4):
    x = int(s[i])
    if next != x:
        isOk = False
        break
    next = (x + 1) % mod

if isOk:
    print("Weak")
else:
    print("Strong")
