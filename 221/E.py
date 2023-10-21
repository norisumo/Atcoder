class BIT():
    def __init__(self, max_n, n):
        self.n = n
        self.bit = [0] * (max_n+1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        print("n:", self.n)
        while i <= self.n:
            print("i:", i)
            self.bit[i] += x
            i += i & -i




N = int(input())
A = list(map(int, input().split()))
mod = 998244353
ma = max(A)

mp = {}
for i in range(N):
    mp[A[i]] = 0

m = 0
for k in mp.keys():
    m += 1
    mp[k] += m

bit = BIT(ma,N)
ans = 0
two= 1
itwo = 1

for i in range(N):
    x = mp[A[i]]
    ans = ans + (two + bit.sum(x+1) % mod) % mod
    two =  (two * 2) % mod
    itwo = (itwo/2) % mod
    print("x = ", x)
    bit.add(x,itwo)

print(ans%mod)
