N = int(input())
dis = []
a = dict()
u = dict()
for i in range(N):
    s = input()
    dis.append(s)
    a[s[:3]] = i
    u[s[:3]] = i
print(a)
print(u)
