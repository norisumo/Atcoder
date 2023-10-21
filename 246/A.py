x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
ansX = 0
if x1 == x2:
    ansx = x3
elif x2 == x3:
    ansx = x1
else:
    ansx = x2

ansy = 0
if y1 == y2:
    ansy = y3
elif y2 == y3:
    ansy = y1
else:
    ansy = y2
print(ansx, ansy)