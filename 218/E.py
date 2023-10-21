#Union Find
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
    return len(self.roots())


N,M = map(int,input().split())
h = []
uf  = UnionFind(N+1)

for i in range(M):
  a,b,c = map(int,input().split())
  if c >= 0:
    h.append([c,a,b])
  else:
    uf.union(a,b)
  
h.sort()
ans = 0
for c,a,b in h:
  if uf.same(a,b):
    ans += c
  else:
    uf.union(a,b)

print(ans)
