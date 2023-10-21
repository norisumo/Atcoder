N = int(input())

def func(a, b):
    return a**3 + a**2 * b + a * b ** 2 + b ** 3

ans = 1 << 60
j = 10 ** 6
for i in range(10**6 + 1):
    while(func(i,j) >= N and j >= 0):
        ans = min(ans, func(i,j))
        j -= 1
print(ans)
