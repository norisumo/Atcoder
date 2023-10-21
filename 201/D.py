H,W = map(int,input().split())

A = []
for i in range(H):
  A.append(input())

#"+"のところは「1」、"-"のところは「-1」として配列aに入れる
a = [[0] * W for i in range(H)]
for i in range(H):
  for j in range(W):
    if A[i][j] == "+":
      a[i][j] = 1
    else:
      a[i][j] = -1

#dpする。終状態からさかのぼり、dp[0][0]のときのスコアでどちらが勝つか判断。
#dpの中身は「高橋-青木」。スタート地点までさかのぼり、0以上ならば、高橋の方がスコアが大と言うことになる。
INF = 1 << 60
dp = [[-INF] * W for i in range(H)]
dp[H-1][W-1] = 0
for i in reversed(range(H)):
  for j in reversed(range(W)):
    #移動したときは相手のターンになるため、dpの正負を逆転する必要がある("-"つけ、-dp)
    #移動前のマスの分を計算にいれること(a[i][j])
    if i-1 >= 0:
      dp[i-1][j] = max(dp[i-1][j], a[i][j] - dp[i][j])
    if j-1 >= 0:
      dp[i][j-1] = max(dp[i][j-1], a[i][j] - dp[i][j])

score = dp[0][0]
  
if score == 0:
  exit(print("Draw"))
elif score > 0:
  exit(print("Takahashi"))
elif score < 0:
  exit(print("Aoki"))