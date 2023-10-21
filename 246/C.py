N,K,X = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
ans = 0
na = []
for i in range(N):
    a = A[i]
    k = a // X
    n = 0
    if k <= K:
        n += a % X
        K -= k
    else:
        n += (a - K * X)
        K = 0
    ans += n
    na.append(n)

if K > 0:
    na.sort(reverse=True)
    for i in range(K):
        if i >= N:
            break
        ans -= na[i]
print(ans)
    

