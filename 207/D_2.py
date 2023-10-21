N = int(input())
S = [complex(*map(int, input().split())) for _ in range(N)]
T = [complex(*map(int, input().split())) for _ in range(N)]

sumS = sum(S)
sumT = sum(T)
 
for i in range(N):
    S[i] = S[i] * N - sumS
    T[i] = T[i] * N - sumT
 
for a in T:
    if a:
        break
 
for b in S:
    if abs(a) != abs(b):
        continue
    for s in S:
        for t in T:
            if a * s == b * t:
                break
        else:
            break
    else:
        print("Yes")
        exit()
print("No")