S = list(input())

a,b = map(int,input().split())
a -= 1
b -= 1
t = S[a]
S[a] = S[b]
S[b] = t
print("".join(S))
