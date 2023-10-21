from collections import defaultdict

N = int(input())
t = []
for i in range(N):
    x,y = map(int, input().split())
    t.append([x,y])
S = input()

Ll = defaultdict(list)
Rl = defaultdict(list)

for i in range(N):
    x,y = t[i]
    s = S[i]
    if s == 'L':
        Ll[y].append(x)
    else:
        Rl[y].append(x)

for v in Rl.keys():
    if not (v in Ll):
        continue
    n = max(Ll[v])
    m = min(Rl[v])
    if n > m:
        print("Yes")
        exit()
print("No")