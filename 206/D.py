# Union Find
class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * (n+1)

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y:
      return

    if self.parents[x] > self.parents[y]:
      x, y = y, x

    self.parents[x] += self.parents[y]
    self.parents[y] = x

  def size(self, x):
    return -self.parents[self.find(x)]

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]

  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]

  def group_count(self):
    # index 0の分を引いておく
    # self.parents = [-1] * (n+1) と+1しているので
    return len(self.roots()) - 1

N = int(input())
A = list(map(int,input().split()))

RA = list(reversed(A))
ma = max(A)
uf = UnionFind(ma)
m = N // 2
for i in range(m):
  a = A[i]
  ra = RA[i]
  if a != ra:
    uf.union(a,ra)

ans = 0
for i in range(ma+1):
  if i == uf.find(i):
    ans += uf.size(i) - 1

print(ans)
