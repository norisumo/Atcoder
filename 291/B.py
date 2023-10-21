from collections import defaultdict
N = int(input())
S = input()

b = [0,0]
z = defaultdict(list)
z[b] = 1
for s in S:
    if (s == 'R'):
        b[0] += 1
    elif s == 'L':
        b[0] -= 1
    elif s == 'U':
        b[1] += 1
    else:
        b[1] -= 1
    z.add(b)
print(z)


