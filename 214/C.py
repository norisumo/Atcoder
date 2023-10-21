N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

cost = [0] * N
midx = N
minVal = 1 << 60
for i in range(N):
    cost[i] = T[i]

for i in range(2 * N):
    idx = i % N
    s = S[idx]
    t = cost[idx]
    co = t + s
    nidx = (idx + 1) % N
    if cost[nidx] > co:
        cost[nidx] = co
for i in range(N):
    print(cost[i])
