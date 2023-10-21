import itertools
S = input()

ss = set(itertools.permutations(S))
ans = len(ss)

print(ans)