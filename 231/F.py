from typing import Callable, TypeVar

T = TypeVar('T')

class FenwickTree:
    def __init__(self, n: int) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: T) -> None:
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def __sum__(self, r: int) -> T:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

    def sum(self, l: int, r: int) -> T:
        assert 0 <= l <= r <= self._n
        return self.__sum__(r) - self.__sum__(l)

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
mp = dict()
AB = []
neg_B = []
for i in range(N):
    a = A[i]
    b = B[i]
    b *= -1
    AB.append([a,b])
    neg_B.append(b)
    mp[b] = 0

sort_B = sorted(list(set(neg_B)))
j = 0
for b in sort_B:
    mp[b] = j
    j += 1

m = len(mp)
ft = FenwickTree(m)

AB.sort()
cnt = 1
ans = 0
for i in range(N):
    a,b = AB[i]
    mp_b = mp[b]
    ft.add(mp_b,1)
    if 0 <= i < (N-1) and a == AB[i+1][0] and b == AB[i+1][1]:
        cnt += 1
        continue
    ans += ft.sum(0,mp_b+1) * cnt
    cnt = 1

print(ans)



