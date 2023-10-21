import math 
N,A,B = map(int, input().split())

def calc(n):
    t = N // n
    ret = t * (n + n*t) // 2
    print(ret)
    return ret
def lcm(a,b):
    return a * b // math.gcd(a,b)

ans = (1+N) * N // 2
ans -= calc(A)
ans -= calc(B)
ans += calc(lcm(A,B))
print(ans)