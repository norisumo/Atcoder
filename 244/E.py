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


N,M,K,S,T,X = map(int,input().split())
mod = 998244353

uf = UnionFind(N+1)

t = [set() for i in range(N+1)]
for i in range(M):
    u,v = map(int,input().split())
    t[u].add(v)
    t[v].add(u)
    uf.union(u,v)

if not uf.same(S,T):
    print(0)
    exit()

dp = [[[0] * 2 for i in range(N+1)] for j in range(K+1)]

dp[0][S][0] = 1

for i in range(K):
    for j in range(1,N+1):
        for nex in t[j]:
            if nex == X:
                dp[i+1][nex][0] += dp[i][j][1]
                dp[i+1][nex][0] %= mod
                dp[i+1][nex][1] += dp[i][j][0]
                dp[i+1][nex][1] %= mod
            else:
                dp[i+1][nex][0] += dp[i][j][0]
                dp[i+1][nex][0] %= mod
                dp[i+1][nex][1] += dp[i][j][1]
                dp[i+1][nex][1] %= mod

ans = dp[K][T][0]
print(ans)
