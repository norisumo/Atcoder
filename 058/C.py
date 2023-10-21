import copy

N = int(input())

mask = [0] * 26
ca = ord('a')

S = input()

for s in S:
    si = ord(s) - ca
    mask[si] += 1

for i in range(N-1):
    S = input()
    sm = [0] * 26
    for s in S:
        si = ord(s) - ca
        sm[si] += 1
    
    for i in range(26):
        mask[i] = min(mask[i], sm[i])

for i in range(26):
    if mask[i] != 0:
        print(chr(i+ca) * mask[i], end="")

print("")