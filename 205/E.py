N,M,K = map(int, input().split())
mod = 10 ** 9 + 7
def combination(n, k):
    nCk = under = top = 1
    
 
    # 分母
    for i in range(2, k + 1):
        under *= i
        under %= mod
 
    # 分子
    for i in range(k):
        top *= (n - i)
        top %= mod
 
    nCk = top * pow(under, mod - 2, mod)
 
    return nCk % mod


if N > M + K:
    exit(print(0))
 
ans = combination(N+M, N)
if K < N:
    ans -= combination(N+M, N-(K+1))
 
print(ans%mod)