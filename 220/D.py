N = int(input())
A = list(map(int, input().split()))
d = [0] * 10
mod = 998244353

ao = A[0]
d[ao] = 1
for i in range(1,N):
    an = A[i]
    nd = [0] * 10
    for j in range(10):
        if d[j] != 0:
            ao = j
            t = ao * an % 10
            s = (ao + an) % 10
            nd[t] += d[ao] % mod
            nd[s] += d[ao] % mod
    d = nd

for i in range(10):
    print(d[i] % mod)






