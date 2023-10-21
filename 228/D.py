Q = int(input())
N = 2 ** 20

A = [-1] * N
P = [i for i in range(N+1)]

def Union(a,b):
  if b < a:
    a,b = b,a
  P[a] = find(b)

def find(n):
  if P[n] == n:
    return n
  P[n] = find(P[n])
  if P[n] == N:
    P[n] = find(P[0])
  return P[n]

for i in range(Q):
  t,x = map(int,input().split())
  if t == 2:
    print(A[x%N])
  else:
    h = find(x%N)
    A[h] = x
    Union(h,h+1)

