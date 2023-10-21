N = int(input())
t = [set() for i in range(N)]

for i in range(N-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    t[a].add(b) 
    t[b].add(a)

c = []
for i in range(N):
    if len(t[i]) == 0:
        exit(print("No"))
    
    if len(t[i]) != 1:
        c.append(i)

if len(c) != 1:
    exit(print("No"))
    
n = c[0]
for i in range(N):
    if i == n:
        continue
    k = list(t[i])[0]
    if k != n:
        exit(print("No"))
print("Yes")