N = int(input())

S = set()
for i in range(N):
    tmp = input()
    for j in range(N):
        if tmp[j] == "#":
            S.add((j,i))

T = set()
for i in range(N):
    tmp = input()
    for j in range(N):
        if tmp[j] == "#":
            T.add((j,i))

for _ in range(4):
    mx,my = min(S)
    S = set((x-mx, y-my) for x,y in S)
    mx,my = min(T)
    T = set((x-mx, y-my) for x,y in T)
    if T == S:
        print("Yes")
        exit()
    T = set((y,-x) for x,y in T)

print("No")