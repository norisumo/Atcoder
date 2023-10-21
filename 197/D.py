import math

N = int(input())
x,y = map(int,input().split())
s = complex(x,y)
x,y = map(int,input().split())
t = complex(x,y)

o = (s+t) / 2
rad = 2 * math.pi / N
r = complex(math.cos(rad), math.sin(rad))

ans = o + (s-o) * r
print(ans.real, ans.imag)
