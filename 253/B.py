H,W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())

koma = []
for i in range(H):
    for j in range(W):
        if S[i][j] == 'o':
            koma.append([i,j])

ans = abs(koma[0][0] - koma[1][0]) + abs(koma[0][1] - koma[1][1])

print(ans)