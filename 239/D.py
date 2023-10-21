M = 201
n = [0] * M
n[0] = 1
n[1] = 1
for i in range(2,M):
    if i ** 2 > M:
        break
    for j in range(i*2,M,i):
        n[j] = 1
a,b,c,d = map(int,input().split())
for i in range(a,b+1):
    isok = True
    for j in range(c,d+1):
        t = i + j
        if n[t] != 1:
            isok = False
            break
    if isok:
        exit(print("Takahashi"))
print("Aoki ")