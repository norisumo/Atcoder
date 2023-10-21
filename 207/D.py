import numpy as np
from scipy.linalg import norm

N = int(input())

if N == 1:
    exit(print("Yes"))

S = []
T = []
for i in range(N):
    x,y = map(int,input().split())
    S.append(complex(x,y))

for i in range(N):
    x,y = map(int,input().split())
    T.append(complex(x,y))
print(S)
print(T)
print("------------------")
def func(p,o,r):
    k = [[] for i in range(N)]
    for i in range(N):
        k[i].append(p[i]-o)
        k[i] = k[i]*r

    return sorted(k, key=lambda x: x.real)


for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if norm((S[1]- S[0])) != norm((T[j]-T[i])):
            continue
        na = func(S,S[0],T[j]-T[i])
        nb = func(T,T[i],S[1]-S[0])
        print(na)
        print(nb)
        if na == nb:
            exit(print("Yes"))
print("No")