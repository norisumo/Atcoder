S = list(input())

flag = 0
for s in S:
    if 'a' <= s <= 'z':
        flag |= 0x01

for s in S:
    if 'A' <= s <= 'Z':
        flag |= (0x01 << 1)

if len(S) == len(set(S)):
    flag |= (0x01 << 2)

if flag == 0x07:
    print("Yes")
else:
    print("No")




