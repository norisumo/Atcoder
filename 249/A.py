a,b,c,d,e,f,x = map(int,input().split())
td = 0
if x <= (a+c):
    td = min(a,x) * b
else:
    td = (x // (a+c)) * a * b + min((x % (a+c)), a) * b
ad = 0
if x <= (d+f):
    ad = min(d,x) * e
else:
    ad = (x // (d+f)) * d * e + min((x % (d+f)), d) * e


if td > ad:
    print("Takahashi")
elif td == ad:
    print("Draw")
else:
    print("Aoki")
    
