N,K = map(int, input().split())
mod = 200
for i in range(K):
    if N % mod == 0:
        N = N // mod
    else:
        N = N * 1000 + mod
print(str(N))
