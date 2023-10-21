N = int(input())
ans = 0
t = 0
while 1:
    if 2 ** t > N:
        print(ans)
        exit()
    else:
        ans = t
        t += 1
