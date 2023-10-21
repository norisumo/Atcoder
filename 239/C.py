x1,y1,x2,y2 = map(int,input().split())

t = []
for i in range(x1-2, x1 + 3):
    for j in range(y1-2, y1 + 3):
        if (x1-i) ** 2 + (y1-j)**2 == 5:
            t.append([i,j])

for i,j in t:
    if (x2-i) ** 2 + (y2-j)**2 == 5:
        exit(print("Yes"))
print("No")

