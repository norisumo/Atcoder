a,b = map(int,input().split())
d = (a**2 + b ** 2) ** 0.5

x = a * 1 / d
y = b * 1 / d
print(x,y)