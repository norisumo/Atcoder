S = input()
t = set()
N = len(S)
for i in range(N):
    t.add(S[i:] + S[:i])

for i in range(N):
    t.add(S[:i] + S[i:])

ts = sorted(t)


print(ts[0])
print(ts[-1])