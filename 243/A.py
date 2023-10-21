v,a,b,c = map(int, input().split())
t = a+b+c
v %= t
v -= a
if v < 0:
    print("F")
    exit()

v -= b
if v < 0:
    print("M")
    exit()

v -= c
if v < 0:
    print("T")
    