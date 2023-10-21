N,K = map(int, input().split())

f = []
for i in range(N):
    a,b =  map(int, input().split())
    f.append([a,b])
f.sort()

nid = 0
bid = 0
now = 0
s = f[nid][0]

if K < s:
    exit(print(K))

for i in range(N):
    nex = f[i][0]
    m = f[i][1]
    
    t = (nex - bid)
    if K - t < 0:
        exit(print(now + K))
        
    K = K - t + m
    now += t
    bid = nex

now += K


print(now)