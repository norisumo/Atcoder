W,H,N = map(int,input().split())

minX = 0
maxX = W
minY = 0
maxY = H


def draw(a,x,y):
    global minX,maxX,minY,maxY
    if a == 1:
        minX = max(minX,x)
    elif a == 2:
        maxX = min(maxX,x)
    elif a == 3:
        minY = max(minY,y)
    elif a == 4:
        maxY = min(maxY,y)

for i in range(N):
    x,y,a = map(int,input().split())
    draw(a, x, y)

x = maxX - minX
y = maxY - minY
ans = x * y
if x < 0 or y < 0:
    ans = 0
print(ans)
