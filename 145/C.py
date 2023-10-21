import itertools

N = int(input())
z = []
for i in range(N):
    z.append(list(map(int,input().split())))

z_l = list(itertools.permutations(range(N)))
all = len(z_l)
ans = 0

for i in range(all):
    s = z_l[i][0]
    for j in range(1,N):
        g = z_l[i][j]
        d = ((z[s][0] - z[g][0])**2 + (z[s][1] - z[g][1])**2)
        ans += pow(d,0.5)
        s = g
ans /= all
print(ans)