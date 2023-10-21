N,X,Y = map(int,input().split())
A = list(map(int,input().split()))

def calc(B):
    l = 0
    r = 0
    cntX = 0
    cntY = 0
    ret = 0
    while l != len(B):
        while r !=len(B) and (cntX == 0 or cntY == 0):
            if B[r] == X:
                cntX += 1
            if B[r] == Y:
                cntY += 1
            r += 1
        if cntX > 0 and cntY > 0:
            ret += len(B) + 1 - r
        if B[l] == X:
            cntX -= 1
        if B[l] == Y:
            cntY -= 1
        l += 1
    return ret



i = 0
ans = 0
while i != N:
    B = []
    while i != N and Y <= A[i] <= X:
        B.append(A[i])
        i += 1
    if len(B) != 0:
        ans += calc(B)
    else:
        i += 1
print(ans)
