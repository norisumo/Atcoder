N,M,K = map(int, input().split())

ans = 0
if N == M:
    ans = K
elif N == K:
    ans = M
elif K == M:
    ans = N



print(ans)