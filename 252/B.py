N,K = map(int,input().split())
A = list(map(int,input().split()))
B = set(map(int,input().split()))

M = max(A)
t = []
for i in range(N):
    if A[i] == M:
        t.append(i+1)

for n in t:
    if n in B:
        exit(print("Yes"))
print("No")
