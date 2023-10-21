#Union Find
class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * (n)

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
t = [set() for i in range(N)]
for i in range(M):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  t[a].add(b)

uf = UnionFind(N)
ans = [0] * N
cnt = 0
for i in reversed(range(N)):
  ans[i] = cnt
  cnt += 1
  if t[i] == set():
    continue
  for j in t[i]:
    if uf.same(i,j):
      continue
    cnt -= 1
    uf.union(i,j)

for i in range(N):
  print(ans[i])



