N = int(input())
ans = 0

def f(a,b,c,d):
    return (a-c)**2 + (b-d) ** 2

t = []
for i in range(N):
    t.append(list(map(int, input().split())))

for i in range(N):
    n = t[i]
    for j in range(N):
        m = t[j]
        d = f(n[0],n[1],m[0],m[1])
        ans = max(ans,d)

ans = (ans) ** 0.5
print(ans)