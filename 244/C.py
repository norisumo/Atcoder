N = int(input())
sn = set()
max_n = 2*N+1
for i in range(max_n+1):
    if i % 2 == 0:
        for j in range(1,max_n+1):
            if j in sn:
                continue
            else:
                print(j)
                sn.add(j)
                break
    else:
        a = int(input())
        sn.add(a)
        if a == 0:
            exit()

