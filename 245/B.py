N = int(input())
A = set(map(int, input().split()))

for i in range(2001):
    if not(i in A):
        print(i)
        exit()

