N = int(input())
M = 2*10**5 + 1
d = [0] * (M)

for i in range(N):
    l,r = map(int,input().split())
    d[l] += 1
    d[r] -= 1

now = False
for n in range(1,M):
    d[n] += d[n-1]
    if not now and d[n] != 0:
        print(n, end=' ')
        now = True
    elif now and d[n] == 0:
        print(n)
        now = False
    

