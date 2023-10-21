H,W,C = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))
INF = 1 << 60


ans = INF

#ある点を決めた時、最小となる点が左上と右下にあるとする場合の2通りを試す。
for ri in range(2):
    #dにansのmin候補を保持
    d = [[INF] * W for i in range(H)]
    for i in range(H):
        for j in range(W):
            #配列外参照をしないようif
            if i > 0:
                d[i][j] = min(d[i][j], d[i-1][j])
            if j > 0:
                d[i][j] = min(d[i][j], d[i][j-1])
            ans = min(ans, A[i][j]+(i+j)*C + d[i][j])
            d[i][j] = min(d[i][j], A[i][j]-(i+j)*C)
    #reverseで上下逆転することで右下に来るケースも同じ処理で対応出来る。
    A.reverse()

print(ans)
