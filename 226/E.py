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

# 頂点数と辺の数が同じ連結成分を数える
# ⇒木とサイクルがくっついた構造
# 全体の頂点数と辺の数が同じでも、
# 連結成分で見た際に問の条件を満たさないケースがあるので注意

# 連結成分のみ考えればよい ⇒ Union Findを使う
N,M = map(int, input().split())
mod = 998244353
es = []
uf = UnionFind(N)
# 辺を取得してUnion Findに突っ込む
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    es.append([a,b])
    uf.union(a,b)

# 各連結成分の辺の数を数える
numE = [0] * N
for i in range(M):
    a = es[i][0]
    numE[uf.find(a)] += 1

# 各連結成分の頂点数を数える
numV = [0] * N
for i in range(N):
    numV[uf.find(i)] += 1

ans = 1
for i in range(N):
    # 0の時はUnion Findの親の頂点ではないので無視
    if numV[i] == 0:
        continue
    # 頂点数 == 辺の数ではないとき、実現不可能
    if numV[i] != numE[i]:
        ans = 0
    else:
        # 1サイクルで2通りの向きをカウント出来る
        ans = (ans * 2) % mod
print(ans)