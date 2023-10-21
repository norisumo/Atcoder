mod = 998244353 
N = int(input())

def calc(x,y):
    ret = (((x+y)%mod) * ((y-x+1) % mod)) // 2
    return ret

ans = 0
t = 1
x = 1
while 1:
    if 10 ** t -1 <= N:
        y = (10**t)%mod - 1
        ans = (ans + calc(1,y-x+1) % mod) % mod
        x = y + 1
    else:
        y = N
        ans = (ans + calc(1,y-x+1) % mod) % mod
        break
    t += 1


print(ans)


