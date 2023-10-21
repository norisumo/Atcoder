N,Q = map(int,input().split())
i_l = list(range(N))
n_l = list(range(N))

for i in range(Q):
    x = int(input())
    x -= 1
    idx = i_l[x]
    nidx = 0
    if idx + 1 == N:
        nidx = idx - 1
    else:
        nidx = idx + 1
    nex = n_l[nidx]
    n_l[idx], n_l[nidx] = n_l[nidx], n_l[idx]
    i_l[x],i_l[nex] = i_l[nex], i_l[x]
    
for i in range(N):
    print(n_l[i] + 1, end = ' ')
    
