x,y = map(int, input().split())

if x == y:
    print(x)
else:
    if (x == 0 and y == 1) or (y == 0 and x == 1):
        print(2)
    elif (x == 1 and y == 2) or (x == 2 and y == 1):
        print(0)
    else:
        print(1)
