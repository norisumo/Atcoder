N,X = map(int,input().split())

a = [0] * (N+1)
p = [0] * (N+1)
a[0] = 1
p[0] = 1

for i in range(1,N+1):
    a[i] = 2 * a[i-1] + 3
    p[i] = 2 * p[i-1] + 1


def func(n,x):
    if n <= 0:
        if x <= 0:
            return 0
        else:
            return p[0]
    elif x <= a[n-1] + 1:
        return func(n-1, x-1)
    else:
        return func(n-1, x - (a[n-1] + 2)) + p[n-1] + 1
ans = func(N,X)
print(ans)