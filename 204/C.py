import sys
sys.setrecursionlimit(10**7)
 
N,M = map(int,input().split())
s = [[] for i in range(N+1)]
dp = [-1] * (N+1)
 
for i in range(M):
  x,y = map(int,input().split())
  s[x].append(y)
 
def f(x):
  if dp[x] >= 0:
    return dp[x]
  ret = 0
  for a in s[x]:
    ret = f(a)+1
  dp[x] = ret
  return ret
ans = 0
for i in range(1,N+1,1):
  t = f(i)

print(ans)