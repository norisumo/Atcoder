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


N = int(input())
es = []
ans = 0
for i in range(N-1):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    es.append([w,u,v])

es.sort()
uf = UnionFind(N)
for i in range(N-1):
    w,u,v = es[i]
    ans += w * uf.size(u) * uf.size(v)
    uf.union(u,v)


print(ans)
