mod = 200

def outPut(s):
    a = []
    cnt = 1
    while s:
        if s&0x01:
            a.append(cnt)
        s >>= 1
        cnt += 1
    print(str(len(a)), end="")
    for i in a:
        print(" " + str(i), end="")
    print("")

N = int(input())
A = list(map(int, input().split()))

N = min(N,8)

n2 = 1 << N
st = [0] * mod
for s in range(1,n2):
    x = 0
    for i in range(N):
        if (s>>i)&0x01:
            x = (x + A[i]) % mod
    if st[x] == 0:
        st[x] = s
    else:
        print("Yes")
        outPut(s)
        outPut(st[x])
        exit()
print("No")





