# PDF解説の方法で解く

N,X,Y = map(int,input().split())
X -= 1
Y -= 1
ans = [0] * N
for i in range(N):
    for j in range(i+1,N):
        #d = min(abs(j - i), abs(X-i) + 1 + abs(j-Y), abs(Y-i) + 1 + (j-X))
        d = min(abs(j - i), abs(X-i) + 1 + abs(j-Y))
        ans[d] += 1

for i in range(1,N):
    print(ans[i])

