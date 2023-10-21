N,X,Y = map(int,input().split())

a = 1
b = 0

if N == 1:
    exit(print(0))

for i in reversed(range(1,N)):
    na = a + a * X + b
    nb = (a * X + b) * Y
    a = na
    b = nb

print(b)
