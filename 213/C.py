H,W,N = map(int,input().split())
X,Y = [],[]

for i in range(N):
    h,w = map(int,input().split())
    X.append(h)
    Y.append(w)

Xdict = {x:i+1 for i,x in enumerate(sorted(list(set(X))))}
Ydict = {y:i+1 for i,y in enumerate(sorted(list(set(Y))))}
for i in range(N):
  print(Xdict[X[i]], Ydict[Y[i]])