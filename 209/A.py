N,M = map(int, input().split())
ans = M - N + 1
if ans <= 0:
    ans = 0
print(ans)