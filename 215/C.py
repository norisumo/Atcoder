import itertools

S,k = input().split()
K = int(k)

s = set(list(itertools.permutations(S)))
t = list(s)
t.sort()

print("".join(t[K-1]))