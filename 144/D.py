import math

a,b,x = map(int,input().split())
ans = 0
if x * 2 >= a * a * b:
    ans = math.atan((2*b * a ** 2 - 2 * x) / (a ** 3)) * 180 / math.pi
else:
    ans = (math.pi / 2 - math.atan(2 * x / (a * b**2))) * 180 / math.pi
print(ans)