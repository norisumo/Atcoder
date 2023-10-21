import sys
sys.setrecursionlimit(10**7)

D,N = map(int,input().split())

def func(x):
    if x % 100 != 0:
        return 0
    return func(x//100) + 1

ans = 0
cnt = 0
for i in range(1,100 ** 3*100+1):
    if func(i) == D:
        cnt += 1
    if cnt == N:
        ans = i
        break
print(ans)

