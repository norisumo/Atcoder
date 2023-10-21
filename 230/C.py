N,A,B = map(int,input().split())
P,Q,R,S = map(int,input().split())

H = Q - P + 1
W = S - R + 1
ans = [['.'] * W for i in range(H)]
# 操作1
l = max(1-A, 1-B)
r = min(N-A , N-B)
lA = A + l
rA = A + r

s = max(lA, P)
t = min(rA, Q)
for i in range(s,t+1):
    k = i - A
    j = B + k
    if R <= j <= S:
        iidx = i-P
        jidx = j-R
        ans[iidx][jidx] = '#'


# 操作2
l = max(1-A, B-N)
r = min(N-A , B-1)
lA = A + l
rA = A + r

s = max(lA, P)
t = min(rA, Q)
for i in range(s,t+1):
    k = i - A
    j = B - k
    if R <= j <= S:
        iidx = i-P
        jidx = j-R
        ans[iidx][jidx] = '#'

for i in range(H):
    for j in range(W):
        print(ans[i][j],end='')
    print("")



