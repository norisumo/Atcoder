N = int(input())

def soin(n):
    fs = {}
    fs[1] = 1
    for i in range(2, n, 1):
        if i ** 2 > n:
            break
        x = 0
        while n%i == 0:
            n = n // i
            x += 1
            fs[i] = x
    if n != 1:
        fs[n] = 1
    return fs

ans = 0
for i in range(1,N+1):
    d = soin(i)
    print(d)
    for t in d.keys():
        print(t)
        


