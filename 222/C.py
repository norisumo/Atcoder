N,M = map(int,input().split())
A = []
for i in range(2*N):
  A.append(input())

j = []
for i in range(2*N):
  j.append([0,i])

wina = 1
winb = -1
def judge(a,b):
  ret = 0

  if a == 'G' and b == 'C':
    ret = wina
  elif a == 'C' and b == 'P':
    ret = wina
  elif a == 'P' and b == 'G':
    ret = wina
  elif b == 'G' and a == 'C':
    ret = winb
  elif b == 'C' and a == 'P':
    ret = winb
  elif b == 'P' and a == 'G':
    ret = winb

  return ret

for i in range(M):
  for n in range(0,2*N,2):
    a = j[n][1]
    b = j[n+1][1]
    res = judge(A[a][i], A[b][i])
    if res == wina:
      j[n][0] -= 1
    elif res == winb:
      j[n+1][0] -= 1
  j.sort()


for i in range(2*N):
  print(j[i][1] + 1)
  

