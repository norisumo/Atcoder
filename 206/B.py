N = int(input())
a = 0
for i in range(1,N+1):
    a += i
    if a >= N:
        exit(print(i))