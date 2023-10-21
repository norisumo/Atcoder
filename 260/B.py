from distutils.log import FATAL


N,X,Y,Z = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = []
for i in range(N):
    C.append(A[i] + B[i])

sa = sorted(list(set(A)), reverse=True)
sb = sorted(list(set(B)), reverse=True)
sc = sorted(list(set(C)),reverse=True)

cnt = 0
end = False
ok = []
for a in sa:
    for i in range(N):
        if cnt == X:
            end = True
            break
        if A[i] == a and not(i+1 in ok):
            ok.append(i+1)
            cnt += 1
        
    if end:
        break

cnt = 0
end = False
for b in (sb):
    for i in range(N):
        if cnt == Y:
            end = True
            break
        if B[i] == b and not(i+1 in ok):
            ok.append(i+1)
            cnt += 1
        
    if end:
        break



cnt = 0
end = False
for c in (sc):
    for i in range(N):
        if cnt == Z:
            end = True
            break
        if C[i] == c and not(i+1 in ok):
            ok.append(i+1)
            cnt += 1
        
    if end:
        break

ok.sort()
for ans in ok:
    print(ans)