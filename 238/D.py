T = int(input())

for i in range(T):
    a,s = map(int,input().split())
    n = s - 2 * a
    if n < 0:
        print("No")
        continue
    if (n & a) == 0:
        print("Yes")
    else:
        print("No")
