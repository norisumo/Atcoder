
a,b,c = map(int, input().split())

for i in range(1001):
    if a <= i <= b:
        if i % c == 0:
            print(i)
            exit()

print(-1)