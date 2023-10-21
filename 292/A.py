
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
    
N,M = map(int, input().split())

hen = [0] * (N+1)

uf = UnionFind(N)

for i in range(M):
    u,v = map(int, input().split())
    rootu  = uf.find(u)
    henu = hen[rootu]
      
    rootv = uf.find(v)
    henv = hen[rootv]

    if(rootu == rootv):
        hen[rootu] += 1
        continue
    uf.union(u,v)
    root = uf.find(u)
    hen[root] = 0
    hen[root] = henu + henv + 1


P = uf.roots()

for p in P:
    n = hen[p]
    s = uf.size(p)
    if(p==0):
        continue
    if n == s:
        continue
    else:
        print("No")
        exit()
print("Yes")


