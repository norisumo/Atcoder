N,M = map(int,input().split())
x = 1900 * M + 100 * (N-M)

y = int(x * (2**M))
print(y)
